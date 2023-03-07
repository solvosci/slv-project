# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class DocumentPage(models.Model):
    _inherit = "document.page"

    task_ids = fields.Many2many('project.task')
    task_count = fields.Integer(compute="_compute_task_count")

    def _compute_task_count(self):
        for record in self:
            record.task_count = len(record.task_ids)
