# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

#hr.job is coming from hr_recruitment module

from odoo import models, fields, api

class ResourceHuman(models.Model):
	_name 			= 'ksworkplace.res_human'
	_inherits 		= {'ksworkplace.resource' : 'res_id'}
	_description 	= 'Human Resource'
	
	jobTitle		= fields.Char(required=True)
	res_id			= fields.Many2one('ksworkplace.resource', string="Resource Id", ondelete='cascade', required=True)

