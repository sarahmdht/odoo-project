    # make sure to call it from the init file
from odoo import fields, models

class TemplateManyOne(models.Model):
    _name = 'template.manyone'
    _description = 'Many2One Template'

    name = fields.Char(string='Name')
    # field_id = fields.Many2one('comodel.name', string='field') 
    # it is stated inside the template.py
   