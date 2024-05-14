# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class MisBudget(models.Model):
    _inherit = "mis.budget"

    project_id = fields.Many2one('project.project', string="Project")
    analytic_account_project_id = fields.Many2one('account.analytic.account', related='project_id.analytic_account_id')
