#-*- coding:utf-8 -*-
{
    'name': 'El Salvador - Accounting',
    'version': '3.0',
    'countries': ['SV'],
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the base module to manage the accounting chart for El Salvador.
Flag icon: By Cobaltous - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=58240706
=====================================================================

Agrega una nomenclatura contable para El Salvador. También icluye impuestos.
Adds accounting chart for El Salvador. It also includes taxes.""",
    'author': 'aquíH',
    'website': 'http://www.aquih.com/',
    'depends': ['base', 'account'],
    'data': [
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
    ],
}
