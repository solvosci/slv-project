# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ProjectCloseMonth(models.TransientModel):
    _name="project.close.month.wizard"
    _description="project.close.month.wizard"

    project_ids = fields.Many2many("project.project")
    last_close_date = fields.Date()

    def close_month(self):
        self.project_ids.filtered(lambda x: x.last_close_date < self.last_close_date).write({"last_close_date":self.last_close_date})
