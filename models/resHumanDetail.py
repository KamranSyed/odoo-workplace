# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class WorkplaceResource(models.Model):
	_name 		= 'ksworkplace.resHumanDetail'
	_inherits 	= 'ksworkplace.resource'

	job			= fields.Many2one('hr.job', string="Job Title", required=True)
	resId 		= fields.Many2one('ksworkplace.resource', string="Resource Id", ondelete='cascade', required=True, auto_join=True)

