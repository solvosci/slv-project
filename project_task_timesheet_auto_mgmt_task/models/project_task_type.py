# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    is_management_stage = fields.Boolean(
        string='Is Management State',
        default=False,
    )
