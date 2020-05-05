from odoo import fields, models, api


class ModelName (models.Model):
    _name = 'cm.brand'
    _description = 'brand'

    name = fields.Char('品牌')
    


