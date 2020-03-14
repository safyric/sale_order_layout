# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_place = fields.Many2one('stock.delivery.place')
