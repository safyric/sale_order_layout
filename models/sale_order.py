# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    ports_id = fields.Many2one('stock.ports')

    incoterm = fields.Many2one(
        'stock.incoterms', 'Incoterms',
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions.")

    lead_time = fields.Float(
        'Lead Time', required=True, default=0.0,
        help="Number of days between the order confirmation and the shipping of the products to the customer")
