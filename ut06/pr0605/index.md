## Práctica 0605

* Ya que la práctica contiene el mismo módulo de la práctica anterior añadiré el contenido nuevo.

* formulario.xml:

```python
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Vista de formulario (versión original) -->
    <record id="view_subscription_form" model="ir.ui.view">
        <field name="name">subscription.form</field>
        <field name="model">subscription.management</field>
        <field name="arch" type="xml">
            <form string="Gestión de Suscripciones">
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="customer_id"/>
                        <field name="subscription_code"/>
                    </group>
                    <notebook>
                        <page string="Detalles Básicos">
                            <group>
                                <field name="start_date"/>
                                <field name="end_date"/>
                                <field name="renewal_date"/>
                                <field name="status"/>
                                <field name="is_renewable"/>
                                <field name="auto_renewal"/>
                                <field name="price"/>
                            </group>
                        </page>
                        <page string="Uso">
                            <group>
                                <field name="usage_limit"/>
                                <field name="current_usage"/>
                                <field name="use_percent"/>
                            </group>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>


    <!-- Vista de árbol -->
    <record id="view_subscription_tree" model="ir.ui.view">
        <field name="name">subscription.tree</field>
        <field name="model">subscription.management</field>
        <field name="arch" type="xml">
            <tree string="Suscripciones">
                <field name="name"/>
                <field name="customer_id"/>
                <field name="subscription_code"/>
                <field name="status"/>
            </tree>
        </field>
    </record>

    <!-- Acción -->
    <record id="action_subscription" model="ir.actions.act_window">
        <field name="name">Suscripciones</field>
        <field name="res_model">subscription.management</field>
        <field name="view_mode">tree,form</field>
    </record>


    <!-- Menú -->
    <menuitem id="menu_subscription_root" name="Gestión de Suscripciones" sequence="10"/>
    <menuitem id="menu_subscription" name="Suscripciones" parent="menu_subscription_root" action="action_subscription" sequence="10"/>
</odoo>
```