# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_points = fields.Many2one('stock.delivery.points')

    incoterm = fields.Many2one(
        'stock.incoterms', 'Incoterms',
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions.")

    lead_time = fields.Float(
        'Lead Time', required=True, default=0.0,
        help="Number of days between the order confirmation and the shipping of the products to the customer")

    use_payment_note = fields.Boolean(string='Payment Term Note')
    payment_note = fields.Text(string='Payment Term Note')
    use_incoterms_note = fields.Boolean(string='Incoterms Note')
    incoterms_note = fields.Text(string='Incoterms Note')
    use_leadtime_note = fields.Boolean(string='Lead Time Note')
    leadtime_note = fields.Text(string='Lead Time Note')
    use_other_note = fields.Boolean(string='Other Note')
    other_note = fields.Text(string='Other Note')
    note = fields.Html(string='Terms and Conditions')

class ResConfigSetting(models.Model):
    _inherit = 'res.config.settings'

    sale_note = fields.Html(related='company_id.sale_note', string="Terms & Conditions")
