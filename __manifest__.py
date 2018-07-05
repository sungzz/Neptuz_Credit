# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'Neptuz Credit Custom',
    'version': '1.0',
    'category': 'Credit',
    'website': 'https://www.neptuz.com',
    'description': """
Functional Credit Feature for easy to record Credit Transaction
""",
    'depends': ['report'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/accounting_assert_test_views.xml',
        # 'report/accounting_assert_test_reports.xml',
        # 'data/accounting_assert_test_data.xml',
        # 'report/report_account_test_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
