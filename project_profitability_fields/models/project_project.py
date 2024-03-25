from odoo import _, api, fields, models, exceptions


class ProjectProject(models.Model):
    _inherit = "project.project"
    
    last_close_date = fields.Date()
    estimated_cost = fields.Monetary()
    estimated_income = fields.Monetary()
    margin = fields.Float(
        compute="_compute_margin",
        inverse="_inverse_margin",
        store=True,
    )
    @api.depends("estimated_income", "estimated_cost")
    def _compute_margin(self):
        for project in self:
            project.margin = (
                project.estimated_income
                and (project.estimated_income - project.estimated_cost)/project.estimated_income
                or 0.0
            )
    
    @api.onchange("margin", "estimated_cost")
    def _inverse_margin(self):
        for project in self:
            if project.margin == 1.0:
                raise exceptions.UserError(_("The margin cannot be equal to 100% (1), as this would cause division by zero."))
            elif project.margin > 1.0:
                raise exceptions.UserError(_("The margin cannot be greater than 100%."))
            else:
                project.estimated_income = project.estimated_cost / (1.0 - project.margin)
