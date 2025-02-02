## Práctica 0601

* Para realizar esta práctica he seguido los siguientes pasos:

    * Lo primero hemos habilitado el modo desarrollador. Esta opción la encontraremos dentro de Ajustes.
    * Creamos un directorio en "addons" que he llamado **gestion_productos**
    * Dentro del directorio creado creamos dos archivos: **__ __init__ __.py** y **__ __manifest__ __.py**.
    * En **__ __manifiest__ __.py** ponemos el nombre del módulo(gestion_productos)
    * En Odoo, clickaremos en **Actualizar lista de aplicaciones**.
    * Buscamos en el filtro de búsqueda el nombre de nuestro módulo(gestion_productos)
    * Utilizamos el siguiente comando para acceder al contenedor de Odoo: **docker compose exec odoo bash**.
    * Crearé la estructura del módulo mediante el comando **odoo scaffold**(odoo scaffold gestion_productos /mnt/extra-addons/)
    * A continuación pasaré la estructura de los ficheros que he modificado:
        
        * __ __manifest__ __.py:

```python
# -*- coding: utf-8 -*-
{
    'name': "gestion_productos",

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
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```
* models.py:

```python
from odoo import models, fields

class Product(models.Model):
    _name = 'gestion_productos.product'
    _description = 'Gestión de Productos'

    nombre = fields.Char(string='Nombre del Producto', required=True)
    descripcion = fields.Text(string='Descripción del Producto')
    codigoproducto = fields.Char(string='Código del Producto', required=True)
    imagen = fields.Image(string='Imagen del Producto')

    
    categoria = fields.Selection(
        [
            ('jardin', 'Jardín'),
            ('hogar', 'Hogar'),
            ('electrodomesticos', 'Electrodomésticos')
        ],
        string='Categoría',
        required=True
    )
    destacable = fields.Boolean(string='Producto Destacable', default=False)

   
    precio_venta = fields.Float(string='Precio de Venta', digits=(6, 2))
    stock = fields.Integer(string='Stock Disponible', default=0)

   
    fecha_creacion = fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now, readonly=True)
    fecha_actualizacion = fields.Datetime(string='Fecha de Última Actualización', readonly=True)

    
    activo = fields.Boolean(string='Activo', default=True)
    peso = fields.Float(string='Peso del Producto', digits=(6, 2))
```
* views.xml:

```python
<odoo>
    <record id="view_product_tree" model="ir.ui.view">
        <field name="name">gestion.productos.tree</field>
        <field name="model">gestion_productos.product</field>
        <field name="arch" type="xml">
            <tree>
                <field name="nombre"/>
                <field name="codigoproducto"/>
                <field name="categoria"/>
                <field name="precio_venta"/>
                <field name="stock"/>
                <field name="activo"/>
            </tree>
        </field>
    </record>

    <record id="action_product_list" model="ir.actions.act_window">
        <field name="name">Productos</field>
        <field name="res_model">gestion_productos.product</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem id="menu_product_root" name="Gestión de Productos" />
    <menuitem id="menu_product_list" name="Productos" parent="menu_product_root" action="action_product_list"/>
</odoo>
```
 * [Interfaz](https://imgur.com/a/6MBtv6l)