# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class ShopinvaderVariant(models.Model):
    _inherit = "shopinvader.variant"

    def _prepare_selector_value(self, variant, value):
        res = super()._prepare_selector_value(variant, value)
        if len(variant.images) > 0:
            res.update({"main_image": variant.images[0]})
        else:
            res.update({"main_image": ""})
        return res
