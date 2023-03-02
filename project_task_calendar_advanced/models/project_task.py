# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"

    partner_type = fields.Selection(
        selection=[("internal", "Internal"), ("customer", "Customer")],
        compute="_compute_partner_type",
        store=True,
        help="""
        Indicates task type according to associated partner:
        internal - belongs to an internal project (has no partner)
        customer - the project was linked to a partner
        """,
    )
    partner_type_color_id = fields.Many2one(
        comodel_name="res.partner",
        compute="_compute_partner_type",
        store=True,
        help="""
        Technical field that help us to set a different color for tasks
        depending on their partner_type.
        """,
    )

    date_planned_start = fields.Datetime(
        string="Start at",
        help="""
        For Task Calendar, indicates planned start date for this task
        """,
    )
    date_planned_duration = fields.Float(
        string="Duration (h)",
        compute="_compute_date_planned_duration",
        store=True,
        readonly=False,
        help="""
        For Task Calendar, indicates planned duration for this task
        """,
    )

    @api.depends("partner_id")
    def _compute_partner_type(self):
        """
        "color" attribute for calendar view needs a Many2one field
        We have a selection field instead, so we emulate this assigning
        - OdooBot partner to partner tasks, and
        - Company partner to internal tasks
        """
        instrumental_partner = self.env.ref("base.user_root").partner_id.id
        for task in self:
            task.write({
                "partner_type": (
                    "customer" if task.partner_id
                    else "internal"
                ),
                "partner_type_color_id": (
                    instrumental_partner if task.partner_id
                    else task.company_id.partner_id.id
                ),
            })

    @api.constrains("date_planned_start")
    def _check_date_planned_values(self):
        err_tasks = self.filtered(
            lambda x: x.date_planned_start and not x.date_planned_duration
        )
        if err_tasks:
            raise ValidationError(
                _("You should set a duration for the following tasks: %s")
                %
                ", ".join(err_tasks.mapped("name"))
            )

    @api.depends("date_planned_start")
    def _compute_date_planned_duration(self):
        self.filtered(lambda x: not x.date_planned_start).write({
            "date_planned_duration": 0.0,
        })
