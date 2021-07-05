# Copyright 2021 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ShopinvaderVariant(models.Model):
    _inherit = "shopinvader.variant"
    _order = "sequence,id"

    sequence = fields.Integer(default=10)
