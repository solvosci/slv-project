# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, _, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    sale_order_count = fields.Integer(compute='_compute_sale_order_count')

    def action_open_sale_order_lines(self):
        self.ensure_one()
        action_window = {
            'name': _('Sale Order Lines'),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.line',
            'views': [[False, 'tree'], [False, 'form']],
            'domain': [('order_id.analytic_account_id', '=', self.analytic_account_id.id)],
        }
        
        return action_window

    @api.depends('analytic_account_id')
    def _compute_sale_order_count(self):
        sale_order = self.env['sale.order'].read_group(
            [('analytic_account_id', 'in', self.analytic_account_id.ids)],
            ['analytic_account_id'],
            ['analytic_account_id'] 
        )
        mapped_data = {data['analytic_account_id'][0]: data['analytic_account_id_count'] for data in sale_order}
        for project in self:
            project.sale_order_count = mapped_data.get(project.analytic_account_id.id, 0)

    def action_open_sale_orders(self):
        self.ensure_one()
        action_window = {
            'name': _('Sale Order'),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'views': [[False, 'tree'], [False, 'form']],
            'domain': [('analytic_account_id', '=', self.analytic_account_id.id)],
        }
        
        return action_window
