## Práctica 0501

Para la realización de esta práctica se han seguido los siguientes pasos:

* Lo primero hemos habilitado el modo desarrollador. Esta opción la encontraremos dentro de Ajustes.
* Creamos un directorio en "addons" que he llamado **reserva_salas**
* Dentro del directorio creado creamos dos archivos: **__init__.py** y **__manifest__.py**.
* En **_manifiest__.py** ponemos el nombre del módulo(reserva_salas)
* En Odoo, clickaremos en **Actualizar lista de aplicaciones**.
* Buscamos en el filtro de búsqued el nombre de nuestro módulo(reserva_salas)
* Utilizamos el siguiente comando para acceder al contenedor de Odoo: **docker compose exec odoo bash**.
* Crearé la estructura del módulo mediante el comando **odoo scaffold**(odoo scaffold reserva_salas /mnt/extra-addons/)
* A continuación pasaré la estructura de los ficheros que he modificado:
    
__models.py__:
```python

   # -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReservaSalas(models.Model):
    _name = 'reserva_salas.reserva_salas'
    _description = 'Gestión de reservas de salas'

    nombreSala = fields.Char(string="Nombre de sala")
    capacidad = fields.Integer(string="Capacidad")
    fechaReserva = fields.Date(string="Fecha de reserva")
    reservada = fields.Boolean(string="¿Está reservada?")
    comentarios = fields.Text(string="Comentarios")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
```
__views.xml:__
```python
<odoo>
  <data>
    <!-- Explicit list view definition -->
    <record model="ir.ui.view" id="reserva_salas_list">
      <field name="name">reserva_salas list</field>
      <field name="model">reserva_salas.reserva_salas</field>
      <field name="arch" type="xml">
        <tree editable="top">
          <field name="nombreSala" string="Nombre de sala"/>
          <field name="capacidad" string="Capacidad"/>
          <field name="fechaReserva" string="Fecha de reserva"/>
          <field name="reservada" string="¿Está reservada?"/>
          <field name="comentarios" string="Comentarios"/>
        </tree>
      </field>
    </record>

    <!-- Actions opening views on models -->
    <record model="ir.actions.act_window" id="reserva_salas_action_window">
      <field name="name">Reserva Salas</field>
      <field name="res_model">reserva_salas.reserva_salas</field>
      <field name="view_mode">tree,form</field>
    </record>

    <!-- Top menu item -->
    <menuitem id="menu_gestion_salas" name="Gestión de Salas"/>

    <!-- Menu categories -->
    <menuitem id="menu_salas" 
              name="Salas" 
              parent="menu_gestion_salas"/>
              
    <menuitem id="menu_salas_disponibles" 
              name="Salas Disponibles" 
              parent="menu_salas" 
              action="reserva_salas_action_window"/>
              
    <menuitem id="menu_reservas" 
              name="Reservas" 
              parent="menu_gestion_salas"/>

    <menuitem id="menu_reservas_realizadas" 
              name="Reservas realizadas" 
              parent="menu_reservas" 
              action="reserva_salas_action_window"/>

  </data>
</odoo>
```
* En el archivo **__manifiest.py** descomenté esta línea: 'security/ir.model.access.csv', para poder acceder al módulo.

* [Interfaz del módulo](https://imgur.com/GMaaBmJ)

