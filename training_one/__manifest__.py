{
    'name': 'template',
    'summary': 'template to create new module',
    'version': '19.0.0.1.0',
    'category': 'Uncategorized',
    'author': 'Sara Medhat',
    'depends': ['base'],
    'data': [     
        # security
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # views
        "views/template_views.xml",
        'views/template_manyone_views.xml',
        'views/template_onemany_views.xml',
        'views/template_manymany_views.xml',

        # menus
        "views/template_menus.xml",
    ],
    'demo': ["demo/demo.xml"],
    'application': True,
    'license': 'LGPL-3',
    }