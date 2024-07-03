# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Project Close Forecast Date",
    "summary": """
        Adds new field forecast date in purchase order line.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.2.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project", "purchase_stock", "project_profitability_fields"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_order_views.xml",
        "views/project_project_views.xml",
        "wizard/project_close_month.xml",
    ],
    "installable": True,
}
