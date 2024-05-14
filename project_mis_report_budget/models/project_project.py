# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    mis_budget_ids = fields.One2many('mis.budget', 'project_id', string="Budgets")
