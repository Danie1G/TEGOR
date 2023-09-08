# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    
    date_entry = fields.Date(related='stock_move_id.date_entry', store=True)
    picking_move_id = fields.Many2one(related='stock_move_id.picking_id', store=True)



    @api.constrains('date_entry')
    def _constrains_date_entry(self):

        for record in self:
            if record.id:
                if record.stock_move_id and record.date_entry:
                    record.date = record.date_entry
                    record._compute_amount()
                    record._onchange_date()
                    

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
    