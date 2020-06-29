# Copyright 2020 ForgeFlow
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    shopinvader_slider_ids = fields.One2many(
        "shopinvader.slider",
        "name",
        string="Shopinvader Slider",
    )