from odoo import _,fields,models, api
from odoo.exceptions import UserError, ValidationError

    # make sure to call it from the init file
    
class Template(models.Model):
    _name = 'template.template'
    _description = 'Template'
    
    active = fields.Boolean(default=True)
    

    # add fields here   
    name = fields.Char(string='Name', required=True, help='Enter the name of the template')
    price = fields.Float(string='Price', default=0.0, required=True)
    # sql constraints
    _name_unique = models.Constraint('UNIQUE(name)', 'The name must be unique.')

    # python constraints
    @api.constrains('price')
    def _check_price(self):
        for rec in self:
            if rec.price < 0:
                raise ValidationError(_('The price must be positive.'))

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
                            #  required=True, # make the field mandatory
                            #  readonly=True, # make the field read-only
                             copy=False, # prevent the field from being copied when duplicating a record
                             tracking=True) # track changes to the field
    date = fields.Date(string='Date', default=fields.Date.today, required=True)
    # relationship fields from the many2one model
    relationship_manyone_id = fields.Many2one('template.manyone', string='Template ManyOne')
    offer_ids = fields.One2many('template.onemany', 'template_id', string='Offers')
    many_ids = fields.Many2many('template.manymany', string='Template ManyMany')

# action buttons
    def action_save(self):
        self.ensure_one()
        self.state = 'confirmed'

    def action_delete(self):
        self.ensure_one()
        raise UserError(_('Delete action not implemented'))