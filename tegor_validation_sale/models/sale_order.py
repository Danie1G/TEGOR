# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_confirm(self):
        for order in self:
            location = order.warehouse_id.lot_stock_id.id
            for line in order.order_line:
                if line.product_id.detailed_type == 'product':
                    product = line.product_id
                    ordered_qty = line.product_uom_qty

                    
                    stock_available = self.env['stock.quant'].search([
                        ('product_id','=',product.id),
                        ('location_id','=',location)])

                    quantity_available = 0
                    for record in stock_available:
                        quantity_available += record.quantity


                    if ordered_qty > quantity_available:
                        raise ValidationError(f"No hay suficiente stock disponible para el producto {product.name} en la ubicación de envío.")

        return super(SaleOrder, self).action_confirm()