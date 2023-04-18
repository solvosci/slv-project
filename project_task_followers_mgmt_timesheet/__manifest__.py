# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Project Task - follower type management - extension to timesheets",
    "summary": """
        Easy management for allow users in a task set as follower mode
        - Timesheet extension
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.3.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project_task_followers_mgmt", "hr_timesheet"],
    "data": [
        "security/ir.model.access.csv",
        "security/hr_timesheet_security.xml",
        "views/hr_timesheet_views.xml",
        "views/project_task_views.xml",
        "views/project_task_timesheet_summary_views.xml",
    ],
}
