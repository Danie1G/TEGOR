# -*- coding: utf-8 -*-

{
    "name": "Tegor - Date Entry",
    "version": "17.0.0.0.1",
    "license": "AGPL-3",
    "summary": "Extension de modulo de Stock y account",
    "author": "Centricital",
    "depends": ["account","stock",'base'],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_picking.xml",
        "wizard/date_wizard.xml",
    
    ],
    "application": False,
    'installable': True,
    'auto_install': False
}
