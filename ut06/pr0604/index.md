## Práctica 0604

* Para realizar esta práctica he seguido los siguientes pasos:

    * Lo primero hemos habilitado el modo desarrollador. Esta opción la encontraremos dentro de Ajustes.
    * Creamos un directorio en "addons" que he llamado **subscription**
    * Dentro del directorio creado creamos dos archivos: **__ __init__ __.py** y **__ __manifest__ __.py**.
    * En **__ __manifiest__ __.py** ponemos el nombre del módulo(subscription)
    * En Odoo, clickaremos en **Actualizar lista de aplicaciones**.
    * Buscamos en el filtro de búsqueda el nombre de nuestro módulo(subscription)
    * Utilizamos el siguiente comando para acceder al contenedor de Odoo: **docker compose exec odoo bash**.
    * Crearé la estructura del módulo mediante el comando **odoo scaffold**(odoo scaffold subscription /mnt/extra-addons/)
    * A continuación pasaré la estructura de los ficheros que he modificado:
        
        * __ __manifest__ __.py:

```python
# -*- coding: utf-8 -*-
{
    'name': "subscription",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vista_basica.xml',
        'views/vista_uso.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```

* subscription.py:

```python:
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

```
* vista_basica.xml:

```python:
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record id="view_subscription_tree_basic" model="ir.ui.view">
      <field name="name">subscription list</field>
      <field name="model">subscription.management</field>
      <field name="arch" type="xml">
        <tree decoration-danger="status == 'expired'" decoration-warning="status == 'cancelled'" limit="15">
          <field name="name" string="Nombre"/>
          <field name="customer_id" string="ID"/>
          <field name="subscription_code" string="Código del suscriptor"/>
          <field name="start_date" string="Fecha de inicio"/>
          <field name="end_date" string="Fecha final" widget="remaining_days"/>
          <field name="renewal_date" string="Fecha de renovación"/>
          <field name="status" string="Estado" widget="radio"/>
          <field name="is_renewable" string="¿Se puede renovar?"/>
          <field name="auto_renewal" string="Renovación automática"/>
          <field name="price" string="Precio" attrs="{'invisible': [('status', '=', 'cancelled')]}" />
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record id="action_subscription_basic" model="ir.actions.act_window">
      <field name="name">Suscripciones (Básico)</field>
      <field name="res_model">subscription.management</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_subscription_tree_basic"/>
    </record>

    <!-- Top menu item -->
    <menuitem name="Suscripciones" id="subscription.menu_root" sequence="1"/>

    <!-- Suscripciones Básicas menu category -->
    <menuitem name="Suscripciones Básicas" id="subscription.menu_1" parent="subscription.menu_root" sequence="10"/>

    <!-- Menu item with action linking to the subscription view -->
    <menuitem name="Lista de Suscripciones" id="subscription.menu_1_list" parent="subscription.menu_1" 
              action="action_subscription_basic" sequence="20"/>
  </data>
</odoo>
```
* vista_uso.xml:

```python:
<odoo>
  <data>
    <!-- explicit list view definition -->
    <record id="view_subscription_tree_usage" model="ir.ui.view">
      <field name="name">subscription usage list</field>
      <field name="model">subscription.management</field>
      <field name="arch" type="xml">
        <tree limit ="15">
          <field name="usage_limit" string="Límite de uso" widget = "progressbar"/>
          <field name="current_usage" string="Uso actual" avg="1"/>
          <field name="use_percent" string="Porcentaje de uso"/>
        </tree>
      </field>
    </record>

    <!-- actions opening views on models -->
    <record id="action_subscription_usage" model="ir.actions.act_window">
      <field name="name">Suscripciones (Uso)</field>
      <field name="res_model">subscription.management</field>
      <field name="view_mode">tree,form</field>
      <field name="view_id" ref="view_subscription_tree_usage"/>
    </record>

    <!-- Top menu item -->
    <menuitem name="Suscripciones" id="subscription.menu_root" sequence="1"/>

    <!-- Suscripciones de Uso menu category -->
    <menuitem name="Suscripciones de Uso" id="subscription.menu_2" parent="subscription.menu_root" sequence="20"/>

    <!-- Menu item with action linking to the usage view -->
    <menuitem name="Lista de Uso" id="subscription.menu_2_list" parent="subscription.menu_2" 
              action="action_subscription_usage" sequence="30"/>
  </data>
</odoo>
```
* [Interfaz](https://imgur.com/a/935sx2b)