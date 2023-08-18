# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError



class StockPicking(models.Model):
    _inherit = "stock.picking"


    def button_validate(self):
        for stock in self:
            location = stock.location_id.id
            for line in stock.move_line_ids_without_package:
                product = line.product_id
                ordered_qty = line.qty_done

                
                stock_available = self.env['stock.quant'].search([
                    ('product_id','=',product.id),
                    ('location_id','=',location)])

                quantity_available = 0
                for record in stock_available:
                    quantity_available += record.quantity


                if ordered_qty > quantity_available:
                    raise ValidationError(f"No hay suficiente stock disponible para el producto {product.name} en la ubicación de Origen.")

        return super(StockPicking, self).button_validate()