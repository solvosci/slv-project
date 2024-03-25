# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"
    
    project_date = fields.Date()
    estimated_cost = fields.Monetary()
    estimated_income = fields.Monetary(compute="_compute_estimated_income", readonly=False, store=True)
    margin = fields.Float()

    @api.depends('estimated_cost', 'margin')
    def _compute_estimated_income(self):
        for project in self:
            project.estimated_income = project.estimated_cost * (1 + project.margin / 100)

    @api.onchange('estimated_income')
    def _onchange_estimated_income(self):
        if self.estimated_cost and self.estimated_income:
            self.margin = ((self.estimated_income - self.estimated_cost) / self.estimated_cost) * 100
            
