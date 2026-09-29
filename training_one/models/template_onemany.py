  # make sure to call it from the init file
from odoo import api, fields, models

class TemplateOneMany(models.Model):
    _name = 'template.onemany'
    _description = 'One2many Template'

    name = fields.Char(string='Name')
    acceptance_state = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy=False,
    )
      # child_ids = fields.One2many('child.model', 'parent_id')
    #   field_id = fields.One2many('comodel.name', 'inverse_name_id', domain, context, auto_join)
    partner_id = fields.Many2one('res.partner')
    template_id = fields.Many2one('template.template', string='Template')
    template_manyone_id = fields.Many2one('template.manyone', string='ManyOne', related='template_id.relationship_manyone_id')
    # computed fields
    qty = fields.Float()
    unit_price = fields.Float()
    readonlytotal = fields.Float(compute='_compute_total', store=True)
    inversetotal = fields.Float(compute='_compute_total', inverse='_inverse_total', store=True)

    @api.depends('qty', 'unit_price')
    def _compute_total(self):
        for rec in self:
            value = rec.qty * rec.unit_price
            rec.readonlytotal = value
            rec.inversetotal = value
            
            

    def _inverse_total(self):
       for rec in self:
           if rec.qty:
              rec.unit_price = rec.inversetotal / rec.qty
              
              
    @api.onchange('qty')
    def _onchange_qty(self):
      for rec in self:
        if rec.qty <= 0:
           return {
            'warning': {
                'title': "Warning",
                'message': "The quantity must be greater than zero.",
                'type': 'notification',
            }
        }