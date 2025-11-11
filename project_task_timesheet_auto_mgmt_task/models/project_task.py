# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    is_management_task = fields.Boolean(
        string='Is Management Task',
        default=False,
    )

    def unlink(self):
        projects = None
        for record in self:
            if record.is_management_task:
                projects = self.env["project.project"].browse(record.project_id.id)

        res = super().unlink()

        if projects:
            for project in projects:
                project.sudo().write({'create_mgmt_task': False})

        return res
