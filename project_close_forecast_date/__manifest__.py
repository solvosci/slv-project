# © 2024 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Project Close Forecast Date",
    "summary": """
        Adds new field forecast date in purchase order line.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["project", "purchase_stock", "project_profitability_fields"],
    "data": [
        "views/purchase_order_views.xml",
    ],
    "installable": True,
}
