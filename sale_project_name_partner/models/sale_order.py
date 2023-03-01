# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _timesheet_create_project_prepare_values(self):
        res = super()._timesheet_create_project_prepare_values()
        res["name"] = '%s - %s' % (res["name"], self.order_partner_id.commercial_partner_id.name)
        return res
