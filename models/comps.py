from odoo import fields, models, api


class ModelName (models.Model):
    _name = 'cm.comp'
    _description = 'comp'

    # name = fields.Char('店櫃',required=True)
    name = fields.Many2one('pos.config.name', string='POS名稱')
    date = fields.Date()

    lee = fields.Integer()
    lee_promotions = fields.Text(size=150)
    levis = fields.Integer()
    levis_promotions = fields.Text(size=150)
    edwin = fields.Integer()
    edwin_promotions = fields.Text(size=150)
    blueway = fields.Integer()
    blueway_promotions = fields.Text(size=150)
    brappers = fields.Integer()
    brappers_promotions = fields.Text(size=150)
    bobson = fields.Integer()
    bobson_promotions = fields.Text(size=150)
    bigtrain = fields.Integer()
    bigtrain_promotions = fields.Text(size=150)