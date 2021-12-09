# -*- coding: utf-8 -*-
{
    'name': "Last Submission Time Off",

    'summary': """
        Last Submission Time Off""",

    'description': """
        This AddsOn is used to determine the deadline for submitting leave submissions (based on leave dates)  
    """,

    'author': "MJT",
    'license':'AGPL-3',
    'website': "http://www.metrocomjaddi.com",
    'category': 'Time Off',
    'version': '0.1',
    'images': [
        'static/description/banner.png',
    ],

    'depends': ['base', 'hr_holidays'],

    # always loaded
    'data': [
        'security/last_submission_security.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
