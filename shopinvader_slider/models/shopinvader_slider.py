# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ShopinvaderSlider(models.Model):

    _name = "shopinvader.slider"
    _description = "Shopinvader Slider"
    _inherit = ["shopinvader.image.mixin"]
    _image_field = "image_id"
    _order = "name"

    name = fields.Char(string="Name", store=True, related="title", readonly=False, required=True)
    title = fields.Char()
    description = fields.Html()
    image_path = fields.Char(
        related="image_id.url", store=True, string="Image Medium Url"
    )
    image_id = fields.Many2one(
        "storage.image", store=True, string="Slider Image"
    )
    image_position = fields.Selection(
        selection=[
            ("left", "Left"),
            ("right", "Right"),
            ("top", "Top"),
            ("bottom", "Bottom"),
        ],
        string="Image Position",
        required=True,
        default="left",
    )
