# -*- coding: utf-8 -*-
{
    'name': "opencinema",

    'summary': """
        Prueba de creacion de un modulo personalizado para Odoo en la
        asignatura de Sistemas de Xestion Empresarial""",

    'description': """
        Practicando la creacion de modulos personalizados.
    """,

    'author': "Manuel RG",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/opencinema.xml',

    ],
    
}
