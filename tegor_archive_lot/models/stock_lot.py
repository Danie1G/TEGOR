# -*- coding: utf-8 -*-

from odoo import fields, models, api



class StockLot(models.Model):
    _inherit = "stock.lot"



    active = fields.Boolean('Archivo', compute='_compute_campo_bool', store=True)


    @api.depends('product_qty')
    def _compute_campo_bool(self):
        for record in self:
            if record.product_qty <= 0:
                record.active = False
            else:
                record.active = True
