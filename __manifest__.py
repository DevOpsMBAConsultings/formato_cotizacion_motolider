{
    'name': 'Formato Cotización Moto Líder',
    'version': '18.0.2.1.0',
    'license': 'LGPL-3',
    'summary': 'Custom Sale Order Report and Total Units for Moto Líder',
    'description': """
Customized quotation format and total units calculation for Moto Líder.
========================================================================

Standalone quotation report for Moto Líder:
- Moto Líder branding (logo, colors)
- Product image column in quotation lines
- Product description without SKU
- Company phone, email and DV shown in header
- Total units calculated and displayed on Backend UI & PDF Report
    """,
    'category': 'Sales',
    'author': 'MBA Consultings',
    'website': 'https://mbaconsultings.com',
    'depends': ['sale', 'mba_pa_base'],
    'data': [
        'views/sale_order_views.xml',
        'report/report_saleorder.xml',
    ],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
}
