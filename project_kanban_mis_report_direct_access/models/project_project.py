# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class ProjectProject(models.Model):
    _inherit = "project.project"

    def action_mis_report_preview(self):
        return self.mis_report_instance_id.preview()
