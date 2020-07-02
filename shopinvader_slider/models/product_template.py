# Copyright 2020 ForgeFlow
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    shopinvader_slider_group_ids = fields.Many2many(
        "shopinvader.slider.group",
        string="Shopinvader Slider Group",
    )