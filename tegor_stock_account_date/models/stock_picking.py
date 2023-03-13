# -*- coding: utf-8 -*-

from odoo import fields, models, api


class StockPickingPalet(models.Model):
    _inherit = "stock.picking"

    date_entry = fields.Date('Fecha de Entrada')

   

class Stockmove(models.Model):
    _name="stock.move"

    
    date_entry = fields.Date('Fecha Entrada', compute='compute_date_entry')


    @api.depends('picking_id')
    def compute_date_entry(self):

        for record in self:

            if record.picking_id.date_entry:
                record.date_entry = record.picking_id.date_entry
            else:
                record.date_entry = False





