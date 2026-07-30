{
    'name': 'Formato Cotización Moto Líder',
    'version': '18.0.1.8.0',
    'license': 'LGPL-3',
    'summary': 'Custom Sale Order Report for Moto Líder',
    'description': """
Customized quotation format for Moto Líder.
============================================

Standalone quotation report for Moto Líder (no longer depends on formato_cotizacion):
- Moto Líder branding (logo, colors)
- Product image column in quotation lines
- Product description without SKU
- Company phone, email and DV shown in header
    """,
    'category': 'Sales',
    'author': 'MBA Consultings',
    'website': 'https://mbaconsultings.com',
    'depends': ['sale', 'mba_pa_base'],
    'data': [
        'report/report_saleorder.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
}
