# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class ResourceVehicle(models.Model):
	_name 		= 'ksworkplace.resVehicle'
	_inherits 	= 'ksworkplace.resource'

	name		= fields.Char(required=True)
	resId 		= fields.Many2one('ksworkplace.resource', string="Resource Id", ondelete='cascade', required=True, auto_join=True)

