# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class StockPickingPalet(models.Model):
    _inherit = "stock.picking"

    date_entry = fields.Date('Fecha de Entrada')
    date_entry_check = fields.Boolean('Fecha Recepcion?')

   

class Stockmove(models.Model):
    _inherit="stock.move"

    
    date_entry = fields.Date('Fecha Entrada', related='picking_id.date_entry', store=True)
    