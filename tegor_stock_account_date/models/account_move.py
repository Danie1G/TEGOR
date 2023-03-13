# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    
    date_entry = fields.Date(related='stock_move_id.date_entry','fecha de Entrada',store=True)


    @api.model_create_multi
    def create(self, vals_list):
        
        res_ids = super(AccountMove, self).create(vals_list)

        for rec in res_ids:
            if rec.date_entry:
                rec.date = rec.date_entry
        
        return res_ids