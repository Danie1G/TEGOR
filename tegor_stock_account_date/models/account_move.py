# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError, ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    
    date_entry = fields.Date(related='stock_move_id.date_entry', store=True)


    # @api.model_create_multi
    # def create(self, vals_list):
        
    #     res_ids = super(AccountMove, self).create(vals_list)

    #     for rec in res_ids:
    #         if rec.date_entry:
    #             rec.date = rec.date_entry
        
    #     return res_ids


    @api.depends('invoice_date', 'company_id','date_entry')
    def _compute_date(self):
        for move in self:
            if move.date_entry:
                move.date = move.date_entry
            else:
                if not move.invoice_date:
                    if not move.date:
                        move.date = fields.Date.context_today(self)
                    continue
                accounting_date = move.invoice_date
                if not move.is_sale_document(include_receipts=True):
                    accounting_date = move._get_accounting_date(move.invoice_date, move._affect_tax_report())
                if accounting_date and accounting_date != move.date:
                    move.date = accounting_date
                    # might be protected because `_get_accounting_date` requires the `name`
                self.env.add_to_compute(self._fields['name'], move)