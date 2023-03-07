# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    "name": "Project Task Knowledge",
    "summary": """
        Adds link between tasks and file Knowledge also there's an automatic link created
        during task creation when a Sales Order is created and a service product is involved.
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "14.0.1.0.0",
    "category": "Project",
    "website": "https://github.com/solvosci/slv-project",
    "depends": ["sale_project", "document_page"],
    "data": [
        "views/project_task_knowledge_actions.xml",
        "views/document_page_views.xml",
        "views/product_template_views.xml",
        "views/project_task_views.xml",
    ],
    'installable': True,
}
