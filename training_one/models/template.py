from odoo import fields,models

class Template(models.Model):
    _name = 'template.template'
    _description = 'Template'

    # add fields here   
    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price', default=0.0, required=True)
    type = fields.Selection([(('value1', 'label1')), ('value2', 'label2')], string='Type', required=True)   