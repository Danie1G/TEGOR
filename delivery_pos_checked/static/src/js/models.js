odoo.define('delivery_pos_checked.models', function (require) {
    'use strict';

    var {Order} = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    const CheckedDeliveryPayment = (Order) => class CheckedDeliveryPayment extends Order {
        constructor(obj, options) {
                super(...arguments);
                if (this.pos.config.ship_later) {
                    this.to_ship = true;
                }
            }
            init_from_JSON(json) {
                super.init_from_JSON(...arguments);
                if (this.pos.config.ship_later) {
                    this.to_ship = true;
                }
            }
    }
    Registries.Model.extend(Order, CheckedDeliveryPayment);
});
