# -*- coding: utf-8 -*-
# © 2017 Elico Corp (https://www.elico-corp.com).
# Copyright 2018 Dreambits Technologies Pvt. Ltd. (<http://dreambits.in>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Project Task Categories',
    'summary': 'Allow unique category for Tasks',
    'version': '11.0.1.0.0',
    'author': 'Dreambits Technologies Pvt. Ltd., Elico Corp, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'category': 'Project Management',
    'website': 'https://github.com/OCA/project',
    'depends': [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/project_data.xml',
        'views/project_categ_view.xml',
        'views/project_task_view.xml',
    ],
    'installable': True,
}
