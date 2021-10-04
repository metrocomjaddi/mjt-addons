# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mjt_payroll_ext(models.Model):
#     _name = 'mjt_payroll_ext.mjt_payroll_ext'
#     _description = 'mjt_payroll_ext.mjt_payroll_ext'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
