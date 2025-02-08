# -*- coding: utf-8 -*-
# from odoo import http


# class SubscriptionFinal(http.Controller):
#     @http.route('/subscription_final/subscription_final', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subscription_final/subscription_final/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('subscription_final.listing', {
#             'root': '/subscription_final/subscription_final',
#             'objects': http.request.env['subscription_final.subscription_final'].search([]),
#         })

#     @http.route('/subscription_final/subscription_final/objects/<model("subscription_final.subscription_final"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subscription_final.object', {
#             'object': obj
#         })
