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
    