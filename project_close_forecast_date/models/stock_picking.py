# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        res = super().write(vals)
        if 'scheduled_date' in vals and vals['scheduled_date']:
            purchase_line_ids = self.move_ids_without_package.purchase_line_id
            purchase_line_ids.write({
                'forecast_date': fields.Date.context_today(self, timestamp=self[0].scheduled_date) 
            })
        return res
