# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, _
from dateutil.relativedelta import relativedelta


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def write(self, vals):
        res = super().write(vals)
        if 'last_close_date' in vals and vals['last_close_date']:
            order_line_ids = self.env['purchase.order.line'].sudo().search([
                ('account_analytic_id', 'in', self.analytic_account_id.ids),
                ('order_id.invoice_status', '!=', 'invoiced'),
                ('state', '!=', 'cancel'),
            ])
            if order_line_ids:
                order_line_ids.write({
                    'forecast_date': self[0].last_close_date + relativedelta(days=1)
                })
        return res
