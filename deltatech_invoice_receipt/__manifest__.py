# -*- coding: utf-8 -*-
# ©  2008-2019 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details


{
    "name": "Deltatech Invoice Receipt",
    'version': '12.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "https://www.terrabit.ro",


    "category": "Accounting",
    "depends": [
        "purchase_stock",
    ],

    "data": [
       # 'account_invoice_view.xml'
        'views/invoice_view.xml'
    ],

    "images": ['static/description/main_screenshot.png'],

    "active": False,
    "installable": True,
}
