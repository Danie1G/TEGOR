# -*- coding: utf-8 -*-

from odoo import fields, models, api



class StockPickingPalet(models.Model):
    _inherit = "stock.picking"

    date_entry = fields.Date('Fecha de Entrada')


    def open_date_wizard(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'Seleccionar Fecha',
            'res_model': 'date.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_stock_picking_id': self.id},
        }

