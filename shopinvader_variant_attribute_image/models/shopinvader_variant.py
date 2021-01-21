# Copyright 2020 ForgeFlow S.L.(http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class ShopinvaderVariant(models.Model):
    _inherit = "shopinvader.variant"

    def _prepare_selector_value(self, variant, value):
        res = super()._prepare_selector_value(variant, value)
        res.update({
            "image": value.image_path or "",
        })
        return res
