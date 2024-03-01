# -*- coding: utf-8 -*-
{
    'name': "GymIAX",

    'summary': """
        Módulo principal para la gestión de alumnos y profesores del gimnasio""",

    'description': """
        Este es un módulo de ejemplo para el examen de SGE2024. 
        A completar por los alumnos según las instrucciones dadas
    """,

    'author': "SGE",
    'website': "https://www.gymiax.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
