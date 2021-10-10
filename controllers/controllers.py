# -*- coding: utf-8 -*-
# from odoo import http


# class GestionClubs(http.Controller):
#     @http.route('/gestion_clubs/gestion_clubs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_clubs/gestion_clubs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_clubs.listing', {
#             'root': '/gestion_clubs/gestion_clubs',
#             'objects': http.request.env['gestion_clubs.gestion_clubs'].search([]),
#         })

#     @http.route('/gestion_clubs/gestion_clubs/objects/<model("gestion_clubs.gestion_clubs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_clubs.object', {
#             'object': obj
#         })
