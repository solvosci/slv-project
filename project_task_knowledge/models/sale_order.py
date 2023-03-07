# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _action_confirm(self):
        result = super()._action_confirm()
        for record in self.sudo().tasks_ids.filtered(lambda x: x.sale_line_id.product_id.document_page_id):
            record.document_page_ids = [(4, record.sale_line_id.product_id.document_page_id.id)]
        return result
