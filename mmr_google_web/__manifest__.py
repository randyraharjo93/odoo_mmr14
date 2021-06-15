# -*- coding: utf-8 -*-
# We have dependencies to odoo voip for now because alexandre want to hide this, but later we can remove it
{
    "name": "MMR14 Google Website",
    "version": "1.0",
    'author': 'Randy',
    "description": """
    Need to Change how Google website work
    """,
    "depends": [
        'website',
        ],
    'init_xml': [],
    'update_xml': [
    ],
    'data': [
        'views/res_partner_views.xml'
        ],
    'css': [],
    'js': [],
    'installable': True,
    'qweb': [
        ],
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
