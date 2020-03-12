# -*- coding: utf-8 -*-
{
    'name': "Sale Order Layout Customize",
    'author': "Safyric Co., Ltd.",
    'website': "https://www.safyric.com",
    'version': '12.0.0.4',

	'depends': [
        'sale_management',
        'stock_delivery_points',
    ],

    'data': [
        'views/sale_report_saleorder_document_template.xml',
        'views/sale_order_template.xml',
        'views/sale_stock.xml',
        'views/website_quote_pricing.xml',
	'views/website_quote.xml',
    ],
    'installable': True,
}
