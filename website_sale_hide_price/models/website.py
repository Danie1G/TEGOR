from odoo import fields, models
from odoo.http import request


class Website(models.Model):
    _inherit = "website"

    website_show_price = fields.Boolean(compute="_compute_website_show_price")
    website_hide_price_default_message = fields.Char(
        string="Default Hidden price message")

    def _compute_website_show_price(self):
        for rec in self:
            rec.website_show_price = request.env.user.partner_id.website_show_price
