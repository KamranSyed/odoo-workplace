# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class Workplace(models.Model):
	_name = 'ksworkplace.workplace'

	name 			= fields.Char(required=True)
	description 	= fields.Char()
	type 			= fields.Selection([
			('fixed', 'Fixed'),
			('venue', 'Venue'),
			('vehicle', 'Vehicle'),
			('boat', 'Boat'),
			('aeroplane', 'Aeroplane'),
			('other', 'Other'),
		], required=True, default='fixed',
        help="Type of Workplace.")
    resources		= fields.Many2one('ksworkplace.resource', string="Resources")
	isvirtual		= fields.Boolean('Is Virtual', default=False)
	active			= fields.Boolean('Active?', default=True)
		 
