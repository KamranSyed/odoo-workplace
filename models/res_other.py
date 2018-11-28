# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class ResourceVehicle(models.Model):
	_name 			= 'ksworkplace.res_other'
	_inherits 		= {'ksworkplace.resource' : 'res_id'}
	_description 	= 'Other Resource'

	name			= fields.Char(required=True)
	res_id 			= fields.Many2one('ksworkplace.resource', string="Resource Id", ondelete='cascade', required=True)

