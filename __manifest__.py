# -*- coding: utf-8 -*-
{
    'name': "Sale Order Layout Customize",

    'summary': """Customize Sale Order Layout""",

    'description': """Customize Sale Order Layout""",

    'author': "Safyric Co., Ltd.",
    'website': "https://www.safyric.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': [
        'sale_management',
        'stock_delivery_ports',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_report_saleorder_document_template.xml',
        'views/sale_order_template.xml',
        'views/sale_stock.xml',
        'views/website_quote_pricing.xml',
    ],
    'installable': True,
}
