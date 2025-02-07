## Proyecto
* Para la realización de este proyecto he creado un nuevo menú llamado Métricas.
* El código nuevo para que aparezca la vista será el siguiente:

    * metrics.py:

```python
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
```
* La vista proporcionada será la siguiente:

```python
<odoo>
    <data>

        <menuitem id="menu_principal"
                  name="Métricas"
                  sequence="10"/>

        <menuitem id="menu_metricas"
                  name="Proyectos"
                  parent="menu_principal"
                  action="action_subscription_metrica"
                  sequence="10"/>

        <record id="view_form_subscription_management" model="ir.ui.view">
            <field name="name">subscription.management.form</field>
            <field name="model">subscription.management</field>
            <field name="arch" type="xml">
                <form string="Gestión de Suscripciones">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="customer_id"/>
                            <field name="subscription_code"/>
                            <field name="start_date"/>
                            <field name="end_date"/>
                            <field name="renewal_date"/>
                            <field name="status"/>
                            <field name="is_renewable"/>
                            <field name="auto_renewal"/>
                            <field name="price"/>
                            <field name="usage_limit"/>
                            <field name="current_usage"/>
                            <field name="use_percent"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_tree_subscription_management" model="ir.ui.view">
            <field name="name">subscription.management.tree</field>
            <field name="model">subscription.management</field>
            <field name="arch" type="xml">
                <tree string="Suscripciones">
                    <field name="name"/>
                    <field name="customer_id"/>
                    <field name="subscription_code"/>
                    <field name="start_date"/>
                    <field name="end_date"/>
                    <field name="status"/>
                </tree>
            </field>
        </record>
        <record id="action_subscription_management" model="ir.actions.act_window">
            <field name="name">Gestión de Suscripciones</field>
            <field name="res_model">subscription.management</field>
            <field name="view_mode">tree,form</field>
        </record>

        <record id="view_form_subscription_metrica" model="ir.ui.view">
            <field name="name">subscription.metrica.form</field>
            <field name="model">subscription.metrica</field>
            <field name="arch" type="xml">
                <form string="Métricas de Suscripción">
                    <sheet>
                        <group>
                            <field name="subscription_id"/>
                            <field name="date"/>
                            <field name="active_subscriptions"/>
                            <field name="generated_revenue"/>
                            <field name="renewals"/>
                            <field name="new_subscriptions"/>
                            <field name="cancellations"/>
                            <field name="recurring_clients"/>
                            <field name="new_clients"/>
                            <field name="arpu"/>
                            <field name="renewal_rate"/>
                            <field name="cancellation_rate"/>
                            <field name="conversion_rate"/>
                            <field name="churn_rate"/>
                            <field name="ltv"/>
                            <field name="cac"/>
                            <field name="notes"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_tree_subscription_metrica" model="ir.ui.view">
            <field name="name">subscription.metrica.tree</field>
            <field name="model">subscription.metrica</field>
            <field name="arch" type="xml">
                <tree string="Métricas de Suscripción">
                    <field name="subscription_id"/>
                    <field name="date"/>
                    <field name="active_subscriptions"/>
                    <field name="generated_revenue"/>
                    <field name="renewals"/>
                    <field name="new_subscriptions"/>
                    <field name="cancellations"/>
                    <field name="recurring_clients"/>
                    <field name="new_clients"/>
                    <field name="arpu"/>
                    <field name="renewal_rate"/>
                    <field name="cancellation_rate"/>
                    <field name="conversion_rate"/>
                    <field name="churn_rate"/>
                    <field name="ltv"/>
                    <field name="cac"/>
                </tree>
            </field>
        </record>

        <record id="action_subscription_metrica" model="ir.actions.act_window">
            <field name="name">Métricas de Suscripción</field>
            <field name="res_model">subscription.metrica</field>
            <field name="view_mode">tree,form</field>
        </record>
    </data>
</odoo>
```
[Resultado](https://imgur.com/a/niABXvx)