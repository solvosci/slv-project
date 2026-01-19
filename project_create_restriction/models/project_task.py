# © 2026 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, models, _
from odoo.exceptions import AccessError


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def check_access_rights(self, operation, raise_exception=True):
        user = self.env.user
        group = "project_create_restriction.group_project_create_projects_tasks"
        admin_user = self.env.ref("base.user_root")

        if (
            operation in ("create", "unlink")
            and user != admin_user
            and not user.has_group(group)
        ):
            if raise_exception:
                raise AccessError(
                    _(
                        "You are not allowed to create or delete tasks. "
                    )
                )
            return False

        return super().check_access_rights(operation, raise_exception)
