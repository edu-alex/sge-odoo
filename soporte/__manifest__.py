# -*- coding: utf-8 -*-
{
    'name': "soporte",

    'summary': """
        Módulo para la gestión de incidencias de SGE """,

    'description': """
        Descripción del módulo para la gestión de incidencias de SGE
    """,

    'author': "SGE",
    'website': "https://www.sge.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
