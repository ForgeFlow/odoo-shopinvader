# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ShopinvaderSlider(models.Model):

    _name = 'shopinvader.slider'
    _description = 'Shopinvader Slider'
    _inherit = ["shopinvader.image.mixin"]
    _image_field = "image_id"

    name = fields.Char()
    style = fields.Selection(
        [('slider', 'Slider'), ('carrousel', 'Carrousel')],
        string='Style', required=True, default="slider"
    )
    description = fields.Char()
    image_path = fields.Char(
        related="image_id.image_id.image_medium_url",
        store=True,
        string="Image Medium Url",
    )
    image_id = fields.Many2one(
        "product.image.relation",
        store=True,
        string="Slider Image",
    )
