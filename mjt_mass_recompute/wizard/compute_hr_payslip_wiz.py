# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ComputeHrPayslipWiz(models.TransientModel):
    _name = 'compute.payslip.wiz'

    def compute_selected_payslip(self):
        cr, uid, context = self.env.args
        if context is None:
            context = {}
        if not context.get('active_ids'):
            return {}
        payslip_ids = context.get('active_ids')
        for payslip in self.env['hr.payslip'].browse(payslip_ids):
            payslip.compute_sheet()
        return {}
