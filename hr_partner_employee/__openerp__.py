# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Rui Pedrosa Franco All Rights Reserved
#    http://pt.linkedin.com/in/ruipedrosafranco
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name'          : 'HR - Partner / Employee',
	'version'       : '1.0',
	'category'      : 'Human Resources',
	'description'   : """
                        Deals with the connection between Partners and Employees\n\n
                        - HR Managers can create an employee from the partner's form\n
                        - shows the employee in the partner's form\n
                        - when an employee is created, a user is also created\n
                        - adds an 'employee' field to the partners tree view\n
                        - adds a filter to the employees tree view\n
                        - adds a 'partner' field to the employees tree view\n
                        """,
	'author'        : 'Rui Pedrosa Franco',
	'website'       : 'http://pt.linkedin.com/in/ruipedrosafranco',
	'depends'       : ['hr'],
	'data'          : ['hr_partner_employee_view.xml'],
    'installable'   : True,
    'active'        : False,
}
