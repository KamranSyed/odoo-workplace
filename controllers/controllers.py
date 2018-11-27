# -*- coding: utf-8 -*-
from odoo import http

# class Ksworkplace(http.Controller):
#     @http.route('/ksworkplace/ksworkplace/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ksworkplace/ksworkplace/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ksworkplace.listing', {
#             'root': '/ksworkplace/ksworkplace',
#             'objects': http.request.env['ksworkplace.ksworkplace'].search([]),
#         })

#     @http.route('/ksworkplace/ksworkplace/objects/<model("ksworkplace.ksworkplace"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ksworkplace.object', {
#             'object': obj
#         })