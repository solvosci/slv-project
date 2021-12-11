# © 2021 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Project Task Custom Info",
    "summary": """
        Adds custom information for Project Tasks 
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.1",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project", "base_custom_info"],
    "data": [
        "security/project_task_custom_info_security.xml",
        "views/custom_info_template_views.xml",
        "views/project_task_views.xml",
        "views/project_task_custom_info_menu.xml",
    ],
    'installable': True,
}
