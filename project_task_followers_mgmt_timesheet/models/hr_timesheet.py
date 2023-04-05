# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)

from odoo import fields, models
from odoo.osv import expression


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    def _new_domain_project_id(self):
        """
        Adds original domain defined in "project" addon to new access
        condition added by project_task_followers_mgmt_timesheet addon
        (see record rules for both modules and original
        project._domain_project_id method)
        """
        domain = self._domain_project_id()
        if not self.user_has_groups('hr_timesheet.group_timesheet_manager'):
            new_expression = [
                '&',
                ('privacy_visibility', '=', 'followers'),
                ('task_ids.allowed_user_ids', 'in', self.env.user.ids)
            ]
            new_expression = expression.AND([
                [('allow_timesheets', '=', True)],
                new_expression
            ])
            domain = expression.OR([domain, new_expression])
        return domain

    project_id = fields.Many2one(domain=_new_domain_project_id)
