# -*- coding: utf-8 -*-
{
    "name": "",
    "version": "17.0.0.0.1",
    "category": "product",
    "license": "AGPL-3",
    "description": """
        This module will add field for invoice policy in sale order.
        Invoice policy in odoo, invoice policy, sale invoice policy, invoice policy
    """,
    "depends": ["sale",'product'],
    
    # Author
    'author': 'Centricital.',
 
    "data": [
             "views/product.xml",
            ],
    "installable": True,
    "auto_install": False,
}
