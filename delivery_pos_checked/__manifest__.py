# -*- coding: utf-8 -*-
{
    'name': "delivery_pos_checked",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Centricital",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'delivery_pos_checked/static/src/js/models.js',
            'delivery_pos_checked/static/src/xml/PaymentScreen.xml'
        ],


    },


}
