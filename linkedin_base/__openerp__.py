# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2010 OpenERP Italian Community (<http://www.openerp-italia.org>). 
#    All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Linkedin base',
    'version': '0.1',
    'category': 'Custom',
    'description': """LinkedIn Extension for OpenERP""",
    'author': 'abstract',
    'website': '',
    'license': 'AGPL-3',
    "depends" : [
        'base',
    ],
    "init_xml" : [
    ],
    "update_xml" : [
        'addons/views/linkedin_view.xml',

        # security
        'security/ir.model.access.csv',
    ],
    "demo_xml" : [
    ],
    "active": False,
    "installable": True,
}

