# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Project Task - Calendar Advanced Timesheet Menu",
    "summary": """
        Adds an extra menu with advanced task calendar (provided by 
        project_task_calendar_advanced addon) to Timesheets app.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "14.0.1.1.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project_task_calendar_advanced", "hr_timesheet_sheet"],
    "data": ["views/project_task_calendar_advanced_timesheet_menu.xml"],
    'installable': True,
}
