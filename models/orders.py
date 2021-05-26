# -*- coding: utf-8 -*-

from odoo import models, fields, api


class orders(models.Model):
    _name = 'pharmacy.orders'
    _description = 'pharmacy.orders'
    customer = fields.Text()
    order_lines = fields.Text()
    total = fields.Float()
    date = fields.Date()

  