# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    forecast_date = fields.Date(compute='_compute_forecast_date', store=True, readonly=True)

    @api.depends('date_planned') 
    def _compute_forecast_date(self):
        for record in self:
            record.forecast_date = fields.Date.context_today(self, timestamp=record.date_planned)
