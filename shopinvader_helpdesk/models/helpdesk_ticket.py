# Copyright 2021 ForgeFlow (http://www.forgeflow.com)
# @author Héctor Villarreal <hector.villarreal@forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ShopinvaderHelpdesk(models.Model):
    _inherit = "helpdesk.ticket"

    shopinvader_backend_id = fields.Many2one(
        "shopinvader.backend", "Shopinvader Backend"
    )
