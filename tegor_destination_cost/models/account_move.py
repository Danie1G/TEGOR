# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import date, timedelta
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    
    landed_costs_ids = fields.Many2many('stock.landed.cost', 'account_stock_landed_rel', 'landed_id', 'account_move_id', 
        string='Allowed accounts',

    )

