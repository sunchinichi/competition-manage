# -*- coding: utf-8 -*-
{
    'name': "同業業績管理系統",

    'summary': """
        Winnie & James studio
        Department store solution.
        """,

    'description': """
        百貨業解決方案：
        同業業績管理系統
        1. 記錄各百貨同業業績
        2. 分析比較
    """,

    'author': "Winnie & James studio",
    'website': "http://www.winniejames.studio",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'module_category_point_of_sale',
    'version': '1.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/comps.xml',
        'views/brands.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}