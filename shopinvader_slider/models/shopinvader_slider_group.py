# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ShopinvaderSliderGroup(models.Model):

    _name = "shopinvader.slider.group"
    _description = "Shopinvader Slider Group"
    _inherit = ["shopinvader.image.mixin"]
    _image_field = "background_image_id"
    _order = "sequence"

    name = fields.Char(string="Name", store=True, related="title", readonly=False, required=True)
    title = fields.Char()
    style = fields.Selection(
        [("slider", "Slider"), ("block", "Block")],
        string="Style",
        required=True,
        default="slider",
    )
    font_color = fields.Selection(
        [("black", "Black"), ("white", "White"), ("danger", "Danger")],
        string="Font Color",
        required=True,
        default="black",
    )
    background_image_path = fields.Char(
        related="background_image_id.url",
        store=True,
        string="Background Image Url",
    )
    background_image_id = fields.Many2one(
        "storage.image", store=True, string="Backgroup Group Image"
    )
    display_on_mobile = fields.Boolean()
    display_indicators = fields.Boolean()
    display_controls = fields.Boolean()
    full_width = fields.Boolean()
    slider_ids = fields.Many2many(
        "shopinvader.slider", string="Shopinvader Slider"
    )

    @api.model
    def _get_sequence(self):
        others = self.search([('sequence', '<>', False)], order='sequence desc', limit=1)
        if others:
            return (others[0].sequence or 0) + 1
        return 1

    sequence = fields.Integer('Sequence', default=_get_sequence)
