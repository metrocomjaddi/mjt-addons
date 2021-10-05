# -*- coding: utf-8 -*-
{
    'name': "Re-compute Mass Payslip",

    'summary': """
        Re-compute mass payslip""",

    'description': """
        To re-compute mass payslip at the same time
    """,

    'author': "MJT",
    'license':'AGPL-3',
    'website': "http://www.metrocomjaddi.com",
    'category': 'Payroll',
    'version': '0.1',
    'images': ['static/description/banner.jpg'],
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/compute_hr_payslip_wiz_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
