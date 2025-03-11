# © 2025 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Project Purchase Line Link",
    "summary": """
        Add button in Projects that joins them with the purchase order lines 
        that have the same analytic account as the project.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project_purchase"],
    "data": [
        "views/project_project.xml",
    ],
    "installable": True,
}
