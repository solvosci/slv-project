# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


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
    task_interval_ids = fields.One2many(
        comodel_name="project.task.interval",
        inverse_name="task_id",
        string="Intervals",
    )
    task_interval_count = fields.Integer(
        compute="_compute_task_interval_count",
        store=True,
        string="Interval count",
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

    @api.depends("task_interval_ids")
    def _compute_task_interval_count(self):
        for task in self:
            task.task_interval_count = len(task.task_interval_ids)
