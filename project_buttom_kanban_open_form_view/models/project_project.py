# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, api, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    def action_project_project_view_form(self):
        return{
            'view_mode':'form',
            'res_model':'project.project',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
        }
