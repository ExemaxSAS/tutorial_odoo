# -*- coding: utf-8 -*-
from odoo import http

# class TutorialOdoo(http.Controller):
#     @http.route('/tutorial_odoo/tutorial_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_odoo/tutorial_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_odoo.listing', {
#             'root': '/tutorial_odoo/tutorial_odoo',
#             'objects': http.request.env['tutorial_odoo.tutorial_odoo'].search([]),
#         })

#     @http.route('/tutorial_odoo/tutorial_odoo/objects/<model("tutorial_odoo.tutorial_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_odoo.object', {
#             'object': obj
#         })