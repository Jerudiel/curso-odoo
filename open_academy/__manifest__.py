{
    'name': "open_academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'author': "Odoo Community Association (OCA)",
    'website': "http://www.yourcompany.com",
    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '15.0.0.0.1',

    'depends': ['base'],

    'data': [
        "security/ir.model.access.csv",

        "views/partner.xml",
        "views/course.xml",
        "views/session.xml",

        "data/ir_ui_menu.xml",
        "data/res_groups.xml",
    ],

    'demo': [
        "demo/course.xml",
        "demo/category.xml",
        "demo/res_partner.xml",
        "demo/user.xml",
    ],
}
