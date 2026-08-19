# -*- coding: utf-8 -*-
{
    'name': 'Certificate URL & LinkedIn Share Button',
    'summary': 'Add a certificate URL and a "Add to LinkedIn" button to completed survey certifications.',
    'description': """
Certificate URL & LinkedIn Share Button
========================================
Adds two small, focused features to the Survey (eLearning certification) app:

1. A computed Certificate URL field on completed, passed survey attempts,
   pointing directly to Odoo's built-in certificate PDF report.
2. An "Add to LinkedIn" button on the survey completion page, which opens
   LinkedIn's official "Add Certification" flow pre-filled with the
   certificate name, issuing organization, and certificate URL.

Optionally, set your company's LinkedIn Page ID under
Settings > General Settings > Certificate LinkedIn for a fully verified
organization link. Leave it empty and your company name is used instead —
no configuration is required.

No custom certificate design/layout is included — this module does not
touch how the certificate itself looks. It only exposes the link and the
LinkedIn share action.
""",
    'author': 'Hüseyin Kırtan',
    'website': '',
    'category': 'eLearning',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['survey'],
    'data': [
        'views/survey_certificate_linkedin.xml',
        'views/survey_user_input_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'certificate_linkedin_share/static/src/css/certificate_linkedin.css',
            'certificate_linkedin_share/static/src/js/linkedin_share.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'support': 'huseyinkirtan.dev@gmail.com',
}
