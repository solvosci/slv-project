# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    document_page_ids = fields.Many2many(
        comodel_name="document.page",
        string="Document pages",
    )
    document_page_count = fields.Integer(compute='_compute_document_page_count')

    def _compute_document_page_count(self):
        for record in self:
            record.document_page_count = len(record.document_page_ids)
