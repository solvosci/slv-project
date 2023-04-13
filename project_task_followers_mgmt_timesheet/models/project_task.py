# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    timesheet_summary_ids = fields.One2many(
        comodel_name="project.task.timesheet_summary",
        inverse_name="task_id",
        string="Timesheet Summaries",
    )

    @api.model
    def create(self, values):
        res = super().create(values)
        res._timesheet_summary_process()
        return res

    def write(self, values):
        res = super().write(values)
        fields_change = ["planned_hours", "allowed_user_ids"]
        values_keys = values.keys()
        if any(field in values_keys for field in fields_change):
            self._timesheet_summary_process()
        return res

    def _timesheet_summary_process(self):
        """
        (Re)create timesheet summaries for the tasks
        """
        self_sudo = self.sudo()
        follower_tasks = self_sudo.filtered(
            lambda x: x.project_id.privacy_visibility == "followers"
        )
        for task in follower_tasks:
            users_summary = task.timesheet_summary_ids.mapped("allowed_user_id")
            new_users = (task.allowed_user_ids - users_summary)
            if new_users:
                task.timesheet_summary_ids = [
                    (0, 0, {"allowed_user_id": new_user.id}) for new_user in new_users
                ]
            delete_users = (users_summary - task.allowed_user_ids)
            task.timesheet_summary_ids.filtered(
                lambda x: x.allowed_user_id.id in delete_users.ids
            ).unlink()
            if task.timesheet_summary_ids:
                task.timesheet_summary_ids.write({
                    "hours_planned": task.planned_hours / len(task.allowed_user_ids)
                })
        # Non-followers projects has no summary data
        (self_sudo - follower_tasks).timesheet_summary_ids.unlink()
