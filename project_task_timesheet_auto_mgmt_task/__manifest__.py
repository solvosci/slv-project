# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Project Timesheet Auto Management Task",
    "summary": """
        Automatically creates a default “Project Management” task when timesheets are enabled.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project", "hr_timesheet"],
    "data": [
        "views/project_project_views.xml",
        "views/res_config_settings_views.xml",
    ]
}
