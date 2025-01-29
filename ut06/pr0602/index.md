## Práctica 0602

* Para realizar esta práctica he seguido los siguientes pasos:
    * Lo primero hemos habilitado el modo desarrollador. Esta opción la encontraremos dentro de Ajustes.
    * Creamos un directorio en "addons" que he llamado **library_mc**
    * Dentro del directorio creado creamos dos archivos: **__ __init__ __.py** y **__ __manifest__ __.py**.
    * En **__ __manifiest__ __.py** ponemos el nombre del módulo(library_mc)
    * En Odoo, clickaremos en **Actualizar lista de aplicaciones**.
    * Buscamos en el filtro de búsqueda el nombre de nuestro módulo(library_mc)
    * Utilizamos el siguiente comando para acceder al contenedor de Odoo: **docker compose exec odoo bash**.
    * Crearé la estructura del módulo mediante el comando **odoo scaffold**(odoo scaffold library_mc /mnt/extra-addons/)
    * A continuación pasaré la estructura de los ficheros que he modificado:
        
         * __ __manifest__ __.py:

```python
# -*- coding: utf-8 -*-
{
    'name': "library_mc",

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
        'views/libro_views.xml',
        'views/autor_views.xml',
        'views/socio_views.xml',
        'views/menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```
* autor.py:

```python
from odoo import models, fields

class Autor(models.Model):
    _name = 'library_mc.autor'
    _description = 'Autor de libros'
    
    name = fields.Char(string='Nombre del autor', required=True)
    country_id = fields.Many2one('res.country', string='País de origen') 
    libro_ids = fields.One2many('library_mc.libro', 'author_id', string='Libros escritos')
```
* libro.py:

```python
from odoo import models, fields

class Libro(models.Model):
    _name = 'library_mc.libro'
    _description = 'Modelo para gestionar los libros'

    title = fields.Char(string="Título", required=True)
    author_id = fields.Many2one('library_mc.autor', string="Autor", required=True)
    genre = fields.Selection([
        ('novela', 'Novela'),
        ('drama', 'Drama'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('misterio', 'Misterio'),
        ('terror', 'Terror'),
        ('historico', 'Histórico'),
    ], string="Género", required=True)
    socios_ids = fields.Many2many('library_mc.socio', string="Socios que han tomado el libro prestado")
```
* socio.py:

```python
from odoo import models, fields

class Socio(models.Model):
    _name = 'library_mc.socio'
    _description = 'Socio de la biblioteca'
    
    name = fields.Char(string='Nombre del socio', required=True)
    phone = fields.Char(string='Teléfono')
    libro_ids = fields.Many2many('library_mc.libro', string='Libros prestados')  
```
* autor_views.xml:

```python
<odoo>
    <!-- Acción para la vista de Autores -->
    <record id="action_library_mc_autor" model="ir.actions.act_window">
        <field name="name">Autores</field>
        <field name="res_model">library_mc.autor</field>
        <field name="view_mode">tree,form</field>
        <field name="target">current</field>
    </record>

    <!-- Vista de lista (tree) para los autores -->
    <record id="view_tree_library_mc_autor" model="ir.ui.view">
        <field name="name">library_mc.autor.tree</field>
        <field name="model">library_mc.autor</field>
        <field name="arch" type="xml">
            <tree string="Autores">
                <field name="name" string="Nombre"/>
                <field name="country_id" string="País"/>
            </tree>
        </field>
    </record>
</odoo>
```
* libro_views.xml:

```python
<odoo>
    <!-- Acción para la vista de libros -->
    <record id="action_library_mc_libro" model="ir.actions.act_window">
        <field name="name">Libros</field>
        <field name="res_model">library_mc.libro</field>
        <field name="view_mode">tree,form</field>
        <field name="target">current</field>
    </record>

    <!-- Vista de lista (tree) para los libros -->
    <record id="view_tree_library_mc_libro" model="ir.ui.view">
        <field name="name">library_mc.libro.tree</field>
        <field name="model">library_mc.libro</field>
        <field name="arch" type="xml">
            <tree string="Libros">
                <field name="title" string="Título"/>
                <field name="author_id" string="Autor"/>
                <field name="genre" string="Género"/>
            </tree>
        </field>
    </record>

    <!-- Definir el menú de Libros -->
    <record id="action_library_mc_libro" model="ir.actions.act_window">
        <field name="name">Libros</field>
        <field name="res_model">library_mc.libro</field>
        <field name="view_mode">tree,form</field>
        <field name="target">current</field>
    </record>
</odoo>
```
* menu_views.xml:

```python
<odoo>
    <!-- Menú principal de la biblioteca -->
    <menuitem id="menu_library_mc"
              name="LibreriaMC"
              sequence="1"/>
              
    <!-- Submenú para los Libros -->
    <menuitem id="menu_library_mc_libro"
              name="Libros"
              parent="menu_library_mc"
              action="action_library_mc_libro"
              sequence="10"/>

    <!-- Submenú para los Autores -->
    <menuitem id="menu_library_mc_autor"
              name="Autores"
              parent="menu_library_mc"
              action="action_library_mc_autor"
              sequence="20"/>

    <!-- Submenú para los Socios -->
    <menuitem id="menu_library_mc_socio"
              name="Socios"
              parent="menu_library_mc"
              action="action_library_mc_socio"
              sequence="30"/>
</odoo>
```
* socio_views.xml:

```python
<odoo>
    <!-- Acción para la vista de Socios -->
    <record id="action_library_mc_socio" model="ir.actions.act_window">
        <field name="name">Socios</field>
        <field name="res_model">library_mc.socio</field>
        <field name="view_mode">tree,form</field>
        <field name="target">current</field>
    </record>

    <!-- Vista de lista (tree) para los socios -->
    <record id="view_tree_library_mc_socio" model="ir.ui.view">
        <field name="name">library_mc.socio.tree</field>
        <field name="model">library_mc.socio</field>
        <field name="arch" type="xml">
            <tree string="Socios">
                <field name="name" string="Nombre"/>
                <field name="phone" string="Teléfono"/>
            </tree>
        </field>
    </record>
</odoo>
```