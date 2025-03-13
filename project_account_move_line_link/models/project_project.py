# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, _, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"

    account_move_line_count = fields.Integer(compute='_compute_account_move_line_count')

    @api.depends('analytic_account_id')
    def _compute_account_move_line_count(self):
        account_move_lines = self.env['account.move.line'].read_group(
            [('analytic_account_id', 'in', self.analytic_account_id.ids)],
            ['analytic_account_id'],
            ['analytic_account_id']
        )
        mapped_data = {data['analytic_account_id'][0]: data['analytic_account_id_count'] for data in account_move_lines}
        for project in self:
            project.account_move_line_count = mapped_data.get(project.analytic_account_id.id, 0)

    def action_open_account_move_lines(self):
        self.ensure_one()
        action_window = {
            'name': _('Account Move Line'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.move.line',
            'views': [[False, 'tree'], [False, 'form']],
            'domain': [('analytic_account_id', '=', self.analytic_account_id.id)],
        }
        return action_window
