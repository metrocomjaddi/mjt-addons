# -*- coding: utf-8 -*-

import logging
import math

from collections import namedtuple

from datetime import datetime, date, timedelta, time
from pytz import timezone, UTC

from odoo import api, fields, models, SUPERUSER_ID, tools
from odoo.addons.base.models.res_partner import _tz_get
from odoo.addons.resource.models.resource import float_to_time, HOURS_PER_DAY
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools import float_compare
from odoo.tools.float_utils import float_round
from odoo.tools.translate import _
from odoo.osv import expression

class HolidaysType(models.Model):
    _inherit = 'hr.leave.type'

    last_submit_date = fields.Integer(
        string='Last Submission Date',
    )

class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    is_editable = fields.Boolean(
        string='Editable',
    )
    is_warning = fields.Boolean(
        string='Warning',
    )

    @api.model_create_multi
    def create(self, vals_list):
        res = super(HolidaysRequest, self).create(vals_list)
        flag = self.env['res.users'].has_group('mjt_last_submission_time_off.group_admin')
        if not flag:
            date_today = fields.Date.today()
            if res.holiday_status_id.last_submit_date > 0:
                date_limit = res.request_date_from + timedelta(days=res.holiday_status_id.last_submit_date)
                if date_limit < date_today:
                    raise ValidationError(_('You must submit time off proposal no later than the start date of time off plus [%s]') %(res.holiday_status_id.last_submit_date))
            elif res.holiday_status_id.last_submit_date < 0:
                date_limit = res.request_date_from + timedelta(days=res.holiday_status_id.last_submit_date)
                if date_limit < date_today:
                    raise ValidationError(_('You must submit time off proposal no later than the start date of time off plus [%s]') %(res.holiday_status_id.last_submit_date))
            res.is_editable =True
        return res

    def write(self, values):
        res = super(HolidaysRequest, self).write(values)
        flag = self.env['res.users'].has_group('mjt_last_submission_time_off.group_admin')
        if not flag:
            date_today = fields.Date.today()
            if self.holiday_status_id.last_submit_date > 0:
                date_limit = self.request_date_from + timedelta(days=self.holiday_status_id.last_submit_date)
                if date_limit < date_today:
                    raise ValidationError(_('You must submit time off proposal no later than the start date of time off plus [%s]') %(self.holiday_status_id.last_submit_date))
            elif self.holiday_status_id.last_submit_date < 0:
                date_limit = self.request_date_from + timedelta(days=self.holiday_status_id.last_submit_date)
                if date_limit < date_today:
                    raise ValidationError(_('You must submit time off proposal no later than the start date of time off plus [%s]') %(self.holiday_status_id.last_submit_date))
        return self

    @api.onchange('date_from', 'date_to', 'employee_id', 'holiday_status_id')
    def onchange_last_submission(self):
        flag = self.env['res.users'].has_group('mjt_last_submission_time_off.group_admin')
        if not flag:
            if self.date_from and self.date_to:
                self.number_of_days = self._get_number_of_days(self.date_from, self.date_to, self.employee_id.id)['days']
                if self.is_editable == True:
                    date_today = fields.Date.today()
                    if self.holiday_status_id.last_submit_date > 0:
                        date_limit = self.request_date_from + timedelta(days=self.holiday_status_id.last_submit_date)
                        if date_limit < date_today:
                            self.is_warning = True
                        else:
                            self.is_warning = False
                    elif self.holiday_status_id.last_submit_date < 0:
                        date_limit = self.request_date_from + timedelta(days=self.holiday_status_id.last_submit_date)
                        if date_limit < date_today:
                            self.is_warning = True
                        else:
                            self.is_warning = False
            else:
                self.number_of_days = 0
                if self.is_editable == True:
                    date_today = fields.Date.today()
                    if self.holiday_status_id.last_submit_date > 0:
                        date_limit = self.request_date_from + timedelta(days=self.holiday_status_id.last_submit_date)
                        if date_limit < date_today:
                            self.is_warning = True
                        else:
                            self.is_warning = False
                    elif self.holiday_status_id.last_submit_date < 0:
                        date_limit = self.request_date_from + timedelta(days=self.holiday_status_id.last_submit_date)
                        if date_limit < date_today:
                            self.is_warning = True
                        else:
                            self.is_warning = False

