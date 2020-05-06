from odoo import fields, models, api


class ModelName (models.Model):
    _name = 'cm.comp'
    _description = 'comp'

    # name = fields.Char('店櫃',required=True)
    name = fields.Many2one('pos.config', string='店櫃名稱')
    date = fields.Date('日期')
    rank = fields.Integer('排名')

    lee = fields.Integer('LEE業績')
    lee_promotions = fields.Text(size=150, string='LEE活動')
    levis = fields.Integer('LEVIS業績')
    levis_promotions = fields.Text(size=150, string='LEVIS活動')
    edwin = fields.Integer('EDWIN業績')
    edwin_promotions = fields.Text(size=150, string='EDWIN活動')
    blueway = fields.Integer('BlueWay業績')
    blueway_promotions = fields.Text(size=150, string='BlueWay活動')
    brappers = fields.Integer('Brappers業績')
    brappers_promotions = fields.Text(size=150, string='Brappers活動')
    bobson = fields.Integer('Bobson業績')
    bobson_promotions = fields.Text(size=150, string='Bobson活動')
    bigtrain = fields.Integer('BigTrain業績')
    bigtrain_promotions = fields.Text(size=150, string='BigTrain活動')
    JohnHerny = fields.Integer('JohnHerny業績')
    JohnHerny_promotions = fields.Text(size=150, string='JohnHerny活動')

    brand_ids = fields.Many2many('cm.brand', string='同業品牌')