{
    'name': 'Formato Cotización Moto Líder',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Custom Sale Order Report for Moto Líder',
    'description': """
Customized quotation format for Moto Líder.
============================================

Extends the base formato_cotizacion module with:
- Moto Líder branding (logo, colors)
- Product image column in quotation lines
- Product description without SKU
    """,
    'category': 'Sales',
    'author': 'MBA Consultings',
    'website': 'https://mbaconsultings.com',
    'depends': ['sale', 'facturacion_electronica'],
    'data': [
        'report/report_saleorder.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
}
