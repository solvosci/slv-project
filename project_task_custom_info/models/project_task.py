# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    _name = "project.task"
    _inherit = [_name, "custom.info"]

    custom_info_template_id = fields.Many2one(context={"default_model": _name})
    custom_info_ids = fields.One2many(context={"default_model": _name})
