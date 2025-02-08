# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SubscriptionMetrica(models.Model):
    _name = 'subscription.metrica'
    _description = 'Métricas de Suscripciones'

    subscription_id = fields.Many2one(
        'subscription.management',
        string='Suscripción',
        required=True
    )
    
    date = fields.Date(
        string='Fecha',
        required=True,
    )

    active_subscriptions = fields.Integer(
        string='Suscripciones Activas',
        compute='_compute_active_subscriptions',
        store=True
    )
    
    generated_revenue = fields.Float(
        string='Ingresos Generados',
        compute='_compute_generated_revenue',
        store=True
    )
    
    renewals = fields.Integer(
        string='Renovaciones',
        compute='_compute_renewals',
        store=True
    )
    
    new_subscriptions = fields.Integer(
        string='Nuevas Suscripciones',
        compute='_compute_new_subscriptions',
        store=True
    )
    
    cancellations = fields.Integer(
        string='Cancelaciones',
        compute='_compute_cancellations',
        store=True
    )
    
    recurring_clients = fields.Integer(
        string='Clientes Recurrentes',
        compute='_compute_clients',
        store=True
    )
    new_clients = fields.Integer(
        string='Clientes Nuevos',
        compute='_compute_clients',
        store=True
    )
    
    arpu = fields.Float(
        string='Ingresos Promedio por Usuario (ARPU)',
        compute='_compute_arpu',
        store=True
    )
    
    renewal_rate = fields.Float(
        string='Tasa de Renovación',
        compute='_compute_renewal_rate',
        store=True
    )

    cancellation_rate = fields.Float(
        string='Tasa de Cancelación',
        compute='_compute_cancellation_rate',
        store=True
    )
    
    conversion_rate = fields.Float(
        string='Tasa de Conversión',
        compute='_compute_conversion_rate',
        store=True
    )
    
    churn_rate = fields.Float(
        string='Tasa de Pérdida de Clientes',
        compute='_compute_churn_rate',
        store=True
    )
    
    ltv = fields.Float(
        string='Lifetime Value (LTV)',
        compute='_compute_ltv',
        store=True
    )
    
    cac = fields.Float(
        string='Costo de Adquisición de Clientes (CAC)',
        compute='_compute_cac',
        store=True
    )
    notes = fields.Text(
        string='Notas',
        help='Comentarios o observaciones sobre las métricas.'
    )
    
    @api.depends('subscription_id')
    def _compute_active_subscriptions(self):
        for record in self:
            record.active_subscriptions = len(record.subscription_id.search([('status', '=', 'active')]))

    @api.depends('subscription_id')
    def _compute_generated_revenue(self):
        for record in self:
            record.generated_revenue = sum(sub.price for sub in record.subscription_id.search([('status', '=', 'active')]))

    @api.depends('subscription_id')
    def _compute_renewals(self):
        for record in self:
            record.renewals = len(record.subscription_id.search([('status', '=', 'active'), ('is_renewable', '=', True)]))

    @api.depends('subscription_id')
    def _compute_new_subscriptions(self):
        for record in self:
            record.new_subscriptions = len(record.subscription_id.search([('status', '=', 'active'), ('start_date', '=', record.date)]))

    @api.depends('subscription_id')
    def _compute_cancellations(self):
        for record in self:
            record.cancellations = len(record.subscription_id.search([('status', '=', 'cancelled'), ('end_date', '=', record.date)]))

    @api.depends('renewals', 'active_subscriptions')
    def _compute_renewal_rate(self):
        for record in self:
            if record.active_subscriptions > 0:
                record.renewal_rate = (record.renewals / record.active_subscriptions) * 100
            else:
                record.renewal_rate = 0

    @api.depends('cancellations', 'active_subscriptions')
    def _compute_cancellation_rate(self):
        for record in self:
            if record.active_subscriptions > 0:
                record.cancellation_rate = (record.cancellations / record.active_subscriptions) * 100
            else:
                record.cancellation_rate = 0

    @api.depends('new_subscriptions', 'active_subscriptions')
    def _compute_conversion_rate(self):
        for record in self:
            if record.active_subscriptions > 0:
                record.conversion_rate = (record.new_subscriptions / record.active_subscriptions) * 100
            else:
                record.conversion_rate = 0

    @api.depends('cancellations', 'active_subscriptions')
    def _compute_churn_rate(self):
        for record in self:
            if record.active_subscriptions > 0:
                record.churn_rate = (record.cancellations / record.active_subscriptions) * 100
            else:
                record.churn_rate = 0

    @api.depends('generated_revenue', 'active_subscriptions')
    def _compute_arpu(self):
        for record in self:
            if record.active_subscriptions > 0:
                record.arpu = record.generated_revenue / record.active_subscriptions
            else:
                record.arpu = 0

    @api.depends('active_subscriptions')
    def _compute_ltv(self):
        for record in self:
            record.ltv = record.arpu * 12  

    @api.depends('new_subscriptions')
    def _compute_cac(self):
        for record in self:

            record.cac = 50.00 

