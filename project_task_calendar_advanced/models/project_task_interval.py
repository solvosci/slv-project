# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectTaskInterval(models.Model):
    _name = "project.task.interval"
    _description = "Task Intervals"
    _inherits = {"project.task": "task_id"}

    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        auto_join=True,
        index=True,
        ondelete="cascade",
        required=True,
    )

    date_planned_start = fields.Datetime(
        string="Start at",
        required=True,
        help="""
        For Task Calendar, indicates planned start date for this task
        """,
    )
    date_planned_duration = fields.Float(
        string="Duration (h)",
        required=True,
        help="""
        For Task Calendar, indicates planned duration for this task
        """,
    )

    @api.constrains("date_planned_start", "date_planned_duration")
    def _check_date_planned_values(self):
        # TODO check intervals overlapping
        err_tasks = self.filtered(
            lambda x: x.date_planned_duration <= 0.0
        )
        if err_tasks:
            raise ValidationError(
                _("You should set a valid duration for the following tasks: %s")
                %
                ", ".join(err_tasks.mapped("name"))
            )
