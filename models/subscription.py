# -*- coding: utf-8 -*-

from odoo import models, fields, api


class subscription(models.Model):
    _name = 'subscription.management'
    _description = 'subscription.subscription'

    name = fields.Char(required=True)
    customer_id = fields.Many2one(
        string='id',
        comodel_name='res.partner',
        required = True,
    )
    subscription_code = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date()
    renewal_date = fields.Date()
    status = fields.Selection(
        string='Estado de la suscripcion',
        selection=[('active', 'active'), ('expired', 'expired'),('pending','pending'),('cancelled','cancelled')]
    )
    
    is_renewable = fields.Boolean()
    auto_renewal = fields.Boolean()
    price = fields.Float()
    usage_limit = fields.Integer()
    current_usage = fields.Integer()
    use_percent = fields.Float()