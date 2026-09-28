  # make sure to call it from the init file
from odoo import fields, models

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
    partner_id = fields.Many2one('res.partner', required=True)
    template_id = fields.Many2one('template.template', string='Template', required=True)
    template_manyone_id = fields.Many2one('template.manyone', string='ManyOne', related='template_id.relationship_manyone_id')