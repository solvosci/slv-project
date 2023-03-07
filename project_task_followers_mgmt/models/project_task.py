# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    allowed_user_ids = fields.Many2many(groups="")
