# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)

        # Crear una línea adicional en la venta cuando el producto tiene configurado uno de reemplazo y su cantidad de stock no es suficiente con el pedido
        for record in res.order_line:
            if record.product_id.secundary_product:
                replacement_product = record.product_id.replacement_product_id
                if record.product_id.qty_available > 0 :
                    if record.product_uom_qty > record.product_id.qty_available:
                        order_line_obj = self.env['sale.order.line']
                        vals = {
                            'order_id': res.id,
                            'product_id': replacement_product.id,
                            'name': replacement_product.name,
                            'product_uom_qty': record.product_uom_qty - record.product_id.qty_available,
                            'product_uom': replacement_product.uom_id.id,
                            'price_unit': replacement_product.lst_price,
                        }
                        record.product_uom_qty = record.product_id.qty_available
                        order_line_obj.create(vals)
                else:
                    record.product_id = replacement_product.id
                  
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id','product_uom_qty')
    def onchange_product_id_qty(self):
        if self.product_id:
            if self.product_id.secundary_product:
                if self.product_uom_qty > self.product_id.qty_available:
                    return {
                            'warning': {
                                'title': _('Stock insuficiente'),
                                'message': _('El %s no cuenta con stock suficiente se usara el producto de reemplazo') % (self.product_id.name)
                                    }
                            }
