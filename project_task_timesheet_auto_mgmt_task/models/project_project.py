# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models, _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    create_mgmt_task = fields.Boolean(
        string="Create management task on project creation",
        help="If enabled, an initial management task will be created with the project.",
        default=False,
    )

    @api.onchange('allow_timesheets')
    def _onchange_allow_timesheets(self):
        for record in self:
            if not record.allow_timesheets:
                record.create_mgmt_task = False
            else:
                record.create_mgmt_task = True

    @api.model_create_multi
    def create(self, vals_list):
        projects = super().create(vals_list)

        self._create_mgmt_task(projects)

        return projects

    def write(self, vals):

        changes = super().write(vals)

        if 'create_mgmt_task' in vals:
            self._create_mgmt_task(self)

        return changes

    def _create_mgmt_task(self, projects):
        Task = self.env["project.task"]
        Stage = self.env["project.task.type"]

        mgmt_stage = Stage.search([('is_management_stage', '=', True)], limit=1)
        if not mgmt_stage:
            mgmt_stage = Stage.create({
                'name': _('Management'),
                'sequence': 1,
                'fold': False,
                'is_management_stage': True,
            })

        for project in projects:

            mgmt_task = project.task_ids.filtered(lambda x: x.is_management_task)

            if project.create_mgmt_task is False and not mgmt_task:
                continue

            if project.create_mgmt_task is False and mgmt_task:
                mgmt_stage.sudo().write({'active': False})
                mgmt_task.sudo().unlink()
                continue

            if project.create_mgmt_task is True and not mgmt_task:
                task_name = project.company_id.task_name or _('[T0] Project Management')
                task_description = project.company_id.task_description or _('Auto-generated management task')
                Task.sudo().create({
                    'name': task_name,
                    'project_id': project.id,
                    'stage_id': mgmt_stage.id,
                    'partner_id': project.partner_id.id or False,
                    'company_id': project.company_id.id,
                    'description': task_description,
                    'is_management_task' : True
                })

        return projects
