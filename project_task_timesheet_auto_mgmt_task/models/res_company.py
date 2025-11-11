# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ResConfigSettings(models.Model):
    _inherit = 'res.company'

    task_name = fields.Char(
        string="Auto management task title",
        translate=True,
        default='[T0] Gestión de Proyecto'
    )
    task_description = fields.Text(
        string="Auto management task description",
        translate=True,
        default='Auto-generated management task'
    )
