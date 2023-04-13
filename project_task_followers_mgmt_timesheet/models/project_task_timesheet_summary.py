# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class ProjectTaskTimesheetSummary(models.Model):
    _name = "project.task.timesheet_summary"
    _description = "Task Timesheet Summaries"
    _inherits = {"project.task": "task_id"}

    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        auto_join=True,
        index=True,
        ondelete="cascade",
        required=True,
    )
    active = fields.Boolean(default=True)
    task_active = fields.Boolean(
        related="task_id.active",
        store=True,
        string="Task active",
    )

    allowed_user_id = fields.Many2one(
        comodel_name="res.users",
        required=True,
        string="User",
    )
    hours_planned = fields.Float()
    hours_effective = fields.Float(
        compute="_compute_hours_effective",
        store=True,
    )
    hours_deviation = fields.Float(
        compute="_compute_hours_deviation",
        store=True,
    )

    @api.depends("timesheet_ids.unit_amount", "allowed_user_id")
    def _compute_hours_effective(self):
        for summary in self:
            summary.hours_effective = sum(
                summary.timesheet_ids.filtered(
                    lambda x: x.user_id == summary.allowed_user_id
                ).mapped("unit_amount")
            )

    @api.depends("hours_planned", "hours_effective")
    def _compute_hours_deviation(self):
        for summary in self:
            summary.hours_deviation = (
                summary.hours_planned - summary.hours_effective
            )
