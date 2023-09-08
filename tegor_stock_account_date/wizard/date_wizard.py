
# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class DateWizard(models.TransientModel):
    _name = 'date.wizard'

    date_field = fields.Date('Fecha de Entrada', required=True)

    stock_picking_id = fields.Many2one('stock.picking', string='stock picking')

    def apply_date(self):
        # Aquí puedes realizar las acciones necesarias para modificar los campos de fecha en los modelos relevantes.
        self.stock_picking_id.write({'date_entry': self.date_field})
        account_moves = self.env['account.move'].search([('ref','ilike', self.stock_picking_id.name)])

        for record in account_moves:
        	record.button_draft()
        	record.write({
        		'name':False,
        		'date':self.date_field})
        	record.action_post()
        return {'type': 'ir.actions.act_window_close'}