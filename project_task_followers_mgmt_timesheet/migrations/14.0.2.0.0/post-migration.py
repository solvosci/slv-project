# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl-3.0.html)
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    """
    Initial timesheet summaries creation for every project
    """
    env["project.project"].with_context(active_test=False).search([
        ("privacy_visibility", "=", "followers"),
    ]).task_ids._timesheet_summary_process()
