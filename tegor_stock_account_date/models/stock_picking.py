# -*- coding: utf-8 -*-

from odoo import fields, models, api


class StockPickingPalet(models.Model):
    _inherit = "stock.picking"

    date_entry = fields.Date('Fecha de Entrada')

   

class Stockmove(models.Model):
    _name="stock.move"

    
    date_entry = fields.Date(related='picking_id.date_entry')

