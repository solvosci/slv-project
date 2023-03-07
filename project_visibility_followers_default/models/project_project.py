# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    privacy_visibility = fields.Selection(default="followers")
