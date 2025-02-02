## Práctica 0701

* Ya que la práctica contiene el mismo módulo de la práctica anterior añadiré el contenido nuevo.

* static_web.xml:

```python
<odoo>
    <template id="static_web" name="Página estática de bienvenida">
        <t t-call="web.html_container">
            <div class="container text-center mt-5" style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);">
                <h1 style="color: #3498db; font-size: 2.5rem; font-family: Arial, sans-serif;">¡Bienvenido a esta página estática!</h1>
                <p style="color: #555; font-size: 1.2rem; margin-top: 10px;">
                    Esperamos que disfrutes explorando este contenido.  
                </p>
            </div>
        </t>
    </template>
</odoo>
```
* dynamic_web.xml:

```python
<odoo>
    <template id="subscription_list_web">
        <t t-call="web.html_container">
            <div class="container">
                <h1>Listado de suscripciones</h1>
                <t t-foreach="suscripciones" t-as="sub">
                    <div class="subs">
                        <span><t t-esc="sub.name"/></span>
                        <span><t t-esc="sub.start_date"/></span>
                    </div>
                </t>
            </div>
        </t>
    </template>
</odoo>
```
* controllers.py:

```python
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json

class Subscription(http.Controller):

    @http.route('/subscription/static', type='http', auth='public', website=True)
    def bienvenida(self, **kwaargs):
        return http.request.render('subscription.static_web', {})

    @http.route('/subscription/dinamic', type='http', auth='public', website=True)
    def subscription_list_web(self, **kwargs):
        sub = http.request.env['subscription.management'].search([])
        return request.render('subscription.subscription_list_web', {
            'suscripciones': sub
        })
```
