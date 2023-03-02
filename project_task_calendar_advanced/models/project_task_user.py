# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import api, fields, models


class ProjectTaskUser(models.Model):
    _name = "project.task.user"
    _description = "Task Calendar Allowed Users"

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Me",
        required=True,
        default=lambda self: self.env.user,
    )
    allowed_user_id = fields.Many2one("res.users", required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        (
            "user_id_allowed_user_id_unique",
            "UNIQUE(user_id, allowed_user_id)",
            "A user cannot have the same allowed user twice."
        ),
    ]

    @api.model
    def unlink_from_allowed_user_id(self, allowed_user_id):
        return self.search([("allowed_user_id", "=", allowed_user_id)]).unlink()
