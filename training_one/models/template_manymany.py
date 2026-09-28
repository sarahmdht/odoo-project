    # make sure to call it from the init file
from odoo import fields, models

class TemplateManyMany(models.Model):
    _name = 'template.manymany'
    _description = 'Many2Many Template'

    name = fields.Char(string='Name')
    # field_id = fields.Many2one('comodel.name', relation, column1, column2) 
    # it is stated inside the template.py
   