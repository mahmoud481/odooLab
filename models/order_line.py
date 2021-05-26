# -*- coding: utf-8 -*-

from odoo import models, fields, api


class order_line(models.Model):
    _name = 'pharmacy.order_line'
    _description = 'pharmacy.order_line'
    name = fields.Many2one('pharmacy.pharmacy','Pharmacy')
    unit_price = fields.Float()
    qty = fields.Integer()
    sub_total = fields.Float()

  