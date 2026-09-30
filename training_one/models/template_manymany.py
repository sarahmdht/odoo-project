    # make sure to call it from the init file
import random

from odoo import fields, models

class TemplateManyMany(models.Model):
    _name = 'template.manymany'
    _description = 'Many2Many Template'
    _order = 'name asc'   # ordering of the records in the list view, default is by id

    

    name = fields.Char(string='Name')
    # field_id = fields.Many2one('comodel.name', relation, column1, column2) 
    # it is stated inside the template.py

# to use color widget
    color = fields.Integer(default=lambda self: self._default_color())

    def _default_color(self):
        used = set(self.search([]).mapped('color'))
        free = [c for c in range(1, 12) if c not in used]
        return random.choice(free) if free else random.randint(1, 11)

    
   