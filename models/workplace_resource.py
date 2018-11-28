# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class WorkplaceResource(models.Model):
	_name = 'ksworkplace.resource'
	_description = 'Abstract Resource'

	qty 			= fields.Integer(string='QTY', required=True, default=1)
	qtymin 			= fields.Integer(string='Min QTY', default=1)
	type 			= fields.Selection([
			('hr', 'Human Resource'),
			('equipment', 'Equipment'),
			('place', 'Place'), 			#e.g Meeting room 3
			('other', 'Other'),
		], default='hr',
        help="Type of Workplace Resource.")		 


#hr, machines etc should be handled separately in thier own classes.
