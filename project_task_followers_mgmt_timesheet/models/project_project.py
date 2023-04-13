# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import models


class ProjectProject(models.Model):
    _inherit = "project.project"

    def write(self, values):
        res = super().write(values)
        if "privacy_visibility" in values.keys():
            self.task_ids._timesheet_summary_process()
        return res
