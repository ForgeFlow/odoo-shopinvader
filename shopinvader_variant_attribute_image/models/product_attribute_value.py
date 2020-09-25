# Copyright 2020 ForgeFlow S.L.(http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ProductAttributeValue(models.Model):
    _name = "product.attribute.value"
    _inherit = ["product.attribute.value", "shopinvader.image.mixin"]
    _image_field = "image_id"

    image_path = fields.Char(
        related="image_id.url", store=True, string="Image Medium Url"
    )
    image_id = fields.Many2one(
        "storage.image", store=True, string="Image"
    )
