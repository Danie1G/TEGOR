# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    secundary_product = fields.Boolean('Producto Opcional')

    replacement_product_id = fields.Many2one('product.product', string='Producto Reemplazable')

   