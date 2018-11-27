# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.
{
    'name': "Workplace",
	'version': '0.7',
    'summary': """
        Helps manage and configure workplace. This workplace could be immovable, movable and virtual.""",

    'description': """
        Helps manage and configure workplace. This workplace could be immovable, movable and virtual. 
    """,

    'author': "Kamran Syed",
    'website': "http://agilesolutionspk.com",
	'license': "GPL-3",
	'installable': True,
    'application': True,
	'auto_install': True,
    'category': 'Human Resources',
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
