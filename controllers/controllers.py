# -*- coding: utf-8 -*-
from odoo import http

# class Competition-manage(http.Controller):
#     @http.route('/competition-manage/competition-manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/competition-manage/competition-manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('competition-manage.listing', {
#             'root': '/competition-manage/competition-manage',
#             'objects': http.request.env['competition-manage.competition-manage'].search([]),
#         })

#     @http.route('/competition-manage/competition-manage/objects/<model("competition-manage.competition-manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('competition-manage.object', {
#             'object': obj
#         })