## Práctica 0502

Para la realización de esta práctica se han seguido los siguientes pasos:

* Lo primero hemos habilitado el modo desarrollador. Esta opción la encontraremos dentro de Ajustes.
* Creamos un directorio en "addons" que he llamado **gestion_biblioteca**
* Dentro del directorio creado creamos dos archivos: **__init__.py** y **__manifest__.py**.
* En **_manifiest__.py** ponemos el nombre del módulo(gestion_biblioteca)
* En Odoo, clickaremos en **Actualizar lista de aplicaciones**.
* Buscamos en el filtro de búsqued el nombre de nuestro módulo(gestion_biblioteca)
* Utilizamos el siguiente comando para acceder al contenedor de Odoo: **docker compose exec odoo bash**.
* Crearé la estructura del módulo mediante el comando **odoo scaffold**(odoo scaffold gestion_biblioteca /mnt/extra-addons/)
* A continuación pasaré la estructura de los ficheros que he modificado:
    
* library_author.py__:

```python
from odoo import models, fields

class library_author(models.Model):
    _name = 'gestion_biblioteca.library_author'
    _description = 'gestion_biblioteca.library_author'

    nombre = fields.Char()
    fecha_nac = fields.Date()
    biografia = fields.Text()
    libros = fields.Text()  
```
* library_book.py:

```python:
from odoo import models, fields

class library_author(models.Model):
    _name = 'gestion_biblioteca.library_author'
    _description = 'gestion_biblioteca.library_author'

    nombre = fields.Char()
    fecha_nac = fields.Date()
    biografia = fields.Text()
    libros = fields.Text()  
```
* library_menu_views.xml:

```python
<odoo>
  <data>
    <!-- Menú raíz -->
    <menuitem name="Biblioteca" id="gestion_biblioteca.menu_root"/>

    <!-- Categorías del menú -->
    <menuitem name="Autores" id="gestion_biblioteca.menu_autor" parent="gestion_biblioteca.menu_root"/>
    <menuitem name="Libros" id="gestion_biblioteca.menu_libro" parent="gestion_biblioteca.menu_root"/>

    <!-- Menús secundarios  -->
    <menuitem name="Lista de Autores" 
              id="gestion_biblioteca.menu_1_autor" 
              parent="gestion_biblioteca.menu_autor"/>

    <menuitem name="Lista de Libros" 
              id="gestion_biblioteca.menu_1_libro" 
              parent="gestion_biblioteca.menu_libro"/>
  </data>
</odoo>
```
* library_book_views.xml:

```python
<odoo>
  <data>
    <!-- Vista de Lista de Libros -->
    <record model="ir.ui.view" id="gestion_biblioteca.library_book_tree_view">
      <field name="name">gestion_biblioteca.library_book.tree</field>
      <field name="model">gestion_biblioteca.library_book</field>
      <field name="arch" type="xml">
        <tree>
          <field name="titulo"/>
          <field name="autor"/>
          <field name="fecha_public"/>
          <field name="isbn"/>
          <field name="sinopsis"/>
        </tree>
      </field>
    </record>

    <!-- Elemento de Menú -->
    <menuitem name="Libros" id="gestion_biblioteca.menu_1_libro" parent="gestion_biblioteca.menu_libro"/>
    
  </data>
</odoo>
```
* library_author_views.xml:

```python
<odoo>
  <data>
    <!-- Vista de Lista de Autores -->
    <record model="ir.ui.view" id="gestion_biblioteca.library_author_tree_view">
      <field name="name">gestion_biblioteca.library_author.tree</field>
      <field name="model">gestion_biblioteca.library_author</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="fecha_nac"/>
          <field name="biografia"/>
          <field name="libros"/>
        </tree>
      </field>
    </record>

    <!-- Elemento de Menú -->
    <menuitem name="Autores" id="gestion_biblioteca.menu_1_autor" parent="gestion_biblioteca.menu_autor"/>

  </data>
</odoo>
```