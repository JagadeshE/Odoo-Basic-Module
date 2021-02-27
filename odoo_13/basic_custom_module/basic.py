# Part of JK. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class basic(models.Model):
	_name = 'basic'
	
	name = fields.Char('Name', size=20, store=True, required=True)
	age = fields.Integer('AGE', size=3,default='')
	gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
        ], string='Gender', default='male')
	birthdate = fields.Date(string='Date Of Birth')
	mobile = fields.Char('Mobile No.', size=15)
	phone = fields.Char('Phone No.', size=15)
	email = fields.Char('Email')
	about = fields.Text(string='About Yourself')
