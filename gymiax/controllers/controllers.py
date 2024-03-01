# -*- coding: utf-8 -*-
# from odoo import http


# class Gymiax(http.Controller):
#     @http.route('/gymiax/gymiax', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gymiax/gymiax/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gymiax.listing', {
#             'root': '/gymiax/gymiax',
#             'objects': http.request.env['gymiax.gymiax'].search([]),
#         })

#     @http.route('/gymiax/gymiax/objects/<model("gymiax.gymiax"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gymiax.object', {
#             'object': obj
#         })
