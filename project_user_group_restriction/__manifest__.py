# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Project User Group Restriction",
    "summary": """
        Hide "Projects" menu from Project Users
        Prevent Project Users from creating tasks
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project"],
    "data": [
        "security/project_security.xml",
        "security/ir.model.access.csv",
        "views/project_menu.xml",
    ],
    'installable': True,
}
