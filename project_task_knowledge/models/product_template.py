# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    document_page_id = fields.Many2one('document.page')
