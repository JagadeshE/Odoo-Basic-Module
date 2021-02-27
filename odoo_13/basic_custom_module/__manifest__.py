# -*- coding: utf-8 -*-
# Part of JK. See LICENSE file for full copyright and licensing details.

{
    'name': 'Basic Custom Module',  
    'description': """  
			Basic Custom module for new menu,form and tree view 
                        +
			It is used for new user or example for creating own module    """,

    'author': 'JK',
    'depends': ['base'],      
    'data': [
		'security/basic_group.xml',
		'security/ir.model.access.csv',
		'views/basic_view.xml'],      
    'application': False, 
}
