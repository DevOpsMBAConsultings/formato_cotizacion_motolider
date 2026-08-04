# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_qty = fields.Float(
        string="Total Unidades",
        compute="_compute_total_qty",
        store=True,
        help="Suma total de unidades de productos en las líneas de la cotización.",
    )

    @api.depends('order_line.product_uom_qty', 'order_line.display_type')
    def _compute_total_qty(self):
        for order in self:
            order.total_qty = sum(
                line.product_uom_qty
                for line in order.order_line
                if not line.display_type
            )
