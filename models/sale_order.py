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

    @api.onchange('sale_order_template_id')
    def _onchange_sale_order_template_id_motolider_pdf(self):
        """
        Auto-assign matching Quote Builder PDF documents when selecting
        a Quotation Template (e.g. Ventas Crédito / Ventas Contado).
        """
        if not self.sale_order_template_id:
            return

        template = self.sale_order_template_id
        doc_ids = []

        # 1. If template has explicit quotation documents attached, use them
        if hasattr(template, 'quotation_document_ids') and template.quotation_document_ids:
            doc_ids = template.quotation_document_ids.ids

        # 2. Search for quotation documents matching template keywords (Crédito / Contado)
        if not doc_ids and 'quotation.document' in self.env:
            template_name = (template.name or '').lower()
            domain = []
            if 'crédito' in template_name or 'credito' in template_name:
                domain = ['|', ('name', 'ilike', 'crédito'), ('name', 'ilike', 'credito')]
            elif 'contado' in template_name:
                domain = [('name', 'ilike', 'contado')]

            if domain:
                docs = self.env['quotation.document'].search(domain, limit=1)
                if docs:
                    doc_ids = docs.ids

        # 3. Assign the matched document(s) to quotation_document_ids
        if doc_ids and hasattr(self, 'quotation_document_ids'):
            self.quotation_document_ids = [(6, 0, doc_ids)]
