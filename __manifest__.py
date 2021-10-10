# -*- coding: utf-8 -*-
{
    'name': "gestion_clubs",

    'summary': "test pratique .....",

    'description': "test pratique ..... ....... .....",

    'author': "Mohamed DAOUD",
    'website': "http://www.daoud-mohamed.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sopte/gestion_clubs',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/equipe.xml',
        'views/entreneur.xml',
        'views/joueur.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
