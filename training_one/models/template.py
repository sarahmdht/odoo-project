from odoo import fields,models
    # make sure to call it from the init file
    
class Template(models.Model):
    _name = 'template.template'
    _description = 'Template'
    
    active = fields.Boolean(default=True, invisible=True)
    

    # add fields here   
    name = fields.Char(string='Name', required=True, help='Enter the name of the template')
    price = fields.Float(string='Price', default=0.0, required=True)
    type = fields.Selection([
        ('value1', 'label1'),
        ('value2', 'label2')
        ], string='Type', required=True)   
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
        ],
                             string='State', # label for the field
                             default='draft', # default value for the field
                             required=True, # make the field mandatory
                             readonly=True, # make the field read-only
                             copy=False, # prevent the field from being copied when duplicating a record
                             tracking=True) # track changes to the field
    date = fields.Date(string='Date', default=fields.Date.today, required=True)
    # relationship fields from the many2one model
    relationship_manyone_id = fields.Many2one('template.manyone', string='Template ManyOne', ondelete='cascade')
    offers_id = fields.One2many('template.onemany', 'template_manyone_id', string='Offers')
    many_id = fields.Many2many('template.manymany', string='Template ManyMany')
    