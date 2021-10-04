# -*- coding: utf-8 -*-
# from odoo import http


# class MjtPayrollExt(http.Controller):
#     @http.route('/mjt_payroll_ext/mjt_payroll_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mjt_payroll_ext/mjt_payroll_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mjt_payroll_ext.listing', {
#             'root': '/mjt_payroll_ext/mjt_payroll_ext',
#             'objects': http.request.env['mjt_payroll_ext.mjt_payroll_ext'].search([]),
#         })

#     @http.route('/mjt_payroll_ext/mjt_payroll_ext/objects/<model("mjt_payroll_ext.mjt_payroll_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mjt_payroll_ext.object', {
#             'object': obj
#         })
