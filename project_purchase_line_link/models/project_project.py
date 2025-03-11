# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, _, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    purchase_order_lines_count = fields.Integer(compute='_compute_purchase_order_lines_count')

    @api.depends('analytic_account_id')
    def _compute_purchase_order_lines_count(self):
        purchase_order_lines = self.env['purchase.order.line'].read_group(
            [('account_analytic_id', 'in', self.analytic_account_id.ids)],
            ['account_analytic_id'],
            ['account_analytic_id']
        )
        mapped_data = {data['account_analytic_id'][0]: data['account_analytic_id_count'] for data in purchase_order_lines}
        for project in self:
            project.purchase_order_lines_count = mapped_data.get(project.analytic_account_id.id, 0)


    def action_open_purchase_lines(self):
        self.ensure_one()
        action_window = {
            'name': _('Purchase Order Lines'),
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order.line',
            'views': [[False, 'tree'], [False, 'form']],
            'domain': [('account_analytic_id', '=', self.analytic_account_id.id)],
        }
        
        return action_window
