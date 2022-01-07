{
    'name': "open_academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        "security/ir.model.access.csv",

        "views/course.xml",

        "data/ir_ui_menu.xml",
    ],

    'demo': [
        "demo/course.xml",
    ],
}
