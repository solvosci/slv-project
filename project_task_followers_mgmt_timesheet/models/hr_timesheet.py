# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, fields, models
from odoo.exceptions import UserError
from odoo.osv import expression


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _new_domain_project_id(self):
        """
        Adds original domain defined in "project" addon to new access
        condition added by project_task_followers_mgmt_timesheet addon
        (see record rules for both modules and original
        project._domain_project_id method)
        """
        domain = self._domain_project_id()
        if not self.user_has_groups('hr_timesheet.group_timesheet_manager'):
            new_expression = [
                '&',
                ('privacy_visibility', '=', 'followers'),
                ('task_ids.allowed_user_ids', 'in', self.env.user.ids)
            ]
            new_expression = expression.AND([
                [('allow_timesheets', '=', True)],
                new_expression
            ])
            domain = expression.OR([domain, new_expression])
        return domain

    project_id = fields.Many2one(domain=_new_domain_project_id)
    # TODO should this field be stored?
    task_summary_id = fields.Many2one(
        comodel_name="project.task.timesheet_summary",
        compute="_compute_task_summary_id",
        help="""
        Technical field for obtaining task summary for this timesheet
        """,
    )
    user_task_finished = fields.Boolean(
        string="User has finished task",
        compute="_compute_user_task_finished",
        inverse="_inverse_user_task_finished",
    )    

    def _compute_task_summary_id(self):
        for timesheet in self:
            timesheet.task_summary_id = timesheet.task_id.timesheet_summary_ids.filtered(
                lambda x: x.allowed_user_id == timesheet.user_id
            ) or False

    def _compute_user_task_finished(self):
        for timesheet in self:
            timesheet.user_task_finished = (
                timesheet.task_summary_id.user_task_finished
                or
                False
            )

    def _inverse_user_task_finished(self):
        for timesheet in self.sudo():
            if timesheet.task_summary_id:
                timesheet.task_summary_id.user_task_finished = timesheet.user_task_finished
            else:
                raise UserError(
                    _("Cannot change task state because you're not assigned to '%s' task")
                    %
                    timesheet.task_id.name
                )
