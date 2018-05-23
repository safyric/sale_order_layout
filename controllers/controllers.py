
# -*- coding: utf-8 -*-
from odoo import http

# class HideWebsiteSalePrice(http.Controller):
#     @http.route('/hide_website_sale_price/hide_website_sale_price/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_website_sale_price/hide_website_sale_price/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_website_sale_price.listing', {
#             'root': '/hide_website_sale_price/hide_website_sale_price',
#             'objects': http.request.env['hide_website_sale_price.hide_website_sale_price'].search([]),
#         })

#     @http.route('/hide_website_sale_price/hide_website_sale_price/objects/<model("hide_website_sale_price.hide_website_sale_price"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_website_sale_price.object', {
#             'object': obj
#         })
