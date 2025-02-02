## Práctica 0601

* Para realizar esta práctica he seguido los siguientes pasos:

    * Lo primero hemos habilitado el modo desarrollador. Esta opción la encontraremos dentro de Ajustes.
    * Creamos un directorio en "addons" que he llamado **stock_management**
    * Dentro del directorio creado creamos dos archivos: **__ __init__ __.py** y **__ __manifest__ __.py**.
    * En **__ __manifiest__ __.py** ponemos el nombre del módulo(stock_management)
    * En Odoo, clickaremos en **Actualizar lista de aplicaciones**.
    * Buscamos en el filtro de búsqueda el nombre de nuestro módulo(stock_management)
    * Utilizamos el siguiente comando para acceder al contenedor de Odoo: **docker compose exec odoo bash**.
    * Crearé la estructura del módulo mediante el comando **odoo scaffold**(odoo scaffold stock_management /mnt/extra-addons/)
    * A continuación pasaré la estructura de los ficheros que he modificado:
        
        * __ __manifest__ __.py:
        
```python
# -*- coding: utf-8 -*-
{
    'name': "stock_management",

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
        'views/stock_products.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```
* stock.product.py:

```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class StockProduct(models.Model):
    _name = 'stock_management.product'
    _description = 'Stock Product'

    name = fields.Char(String = "Nombre del producto")
    category = fields.Selection([('Microprocesadores'),('Memorias'),('Gráficos')],String = "Categoría del producto")
    price = fields.Float(String = "Precio unitario del producto")
    quantity = fields.Integer(String = "Cantidad en stock")
    total_value = fields.Float(String="Valor Total", compute="_compute_total_value", store=True)
    minimum_quantity = fields.Integer(String = "Valor entero")
    stock_status = fields.Selection([
        ('normal', 'Normal'),
        ('low_stock', 'Low Stock')
    ], string="Estado del Stock", compute="_compute_stock_status", store=True)

    full_name = fields.Char(string="Nombre Completo", compute="_compute_full_name", store=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre del producto debe ser único.'),
        ('check_quantity', 'CHECK(quantity >= 0)', 'La cantidad en stock no puede ser negativa.')
    ]
@api.depends('price', 'quantity')
def _compute_total_value(self):
        for record in self:
            record.total_value = record.price * record.quantity

@api.depends('quantity', 'minimum_quantity')
def _compute_stock_status(self):
        for record in self:
            record.stock_status = 'normal' if record.quantity >= record.minimum_quantity else 'low_stock'

@api.depends('name', 'category')
def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.name} ({dict(self._fields['category'].selection).get(record.category)})"

@api.constrains('price', 'quantity', 'total_value', 'category')
def _check_constraints(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("El precio debe ser mayor que 0.")
            if record.quantity < 0:
                raise ValidationError("La cantidad debe ser mayor o igual a 0.")
            if record.total_value > 100000:
                raise ValidationError("El valor total del stock no puede superar las 100000 unidades monetarias.")
            if not record.category:
                raise ValidationError("El producto debe tener una categoría asignada.")
```
* stock_products.xml:

```python
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <!-- Vista de Lista -->
    <record id="view_stock_product_list" model="ir.ui.view">
        <field name="name">stock.product.list</field>
        <field name="model">stock_management.product</field>
        <field name="arch" type="xml">
            <tree string="Productos">
                <field name="name" string="Nombre del Producto"/>
                <field name="category" string="Categoría"/>
                <field name="price" string="Precio Unitario"/>
                <field name="quantity" string="Cantidad en Stock"/>
                <field name="total_value" string="Valor Total" readonly="1"/>
                <field name="stock_status" string="Estado del Stock" readonly="1"/>
            </tree>
        </field>
    </record>

    <!-- Acción para la Vista -->
    <record id="action_stock_product" model="ir.actions.act_window">
        <field name="name">Productos</field>
        <field name="res_model">stock_management.product</field>
        <field name="view_mode">tree,form</field>
    </record>

    <!-- Menú Principal -->
    <menuitem id="menu_stock_management_root" name="Stock Management" sequence="10"/>

    <!-- Submenú para Productos -->
    <menuitem id="menu_stock_product" 
              name="Productos" 
              parent="menu_stock_management_root" 
              action="action_stock_product" 
              sequence="10"/>
</odoo>
```
