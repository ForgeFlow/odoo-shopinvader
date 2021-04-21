# Copyright 2021 ForgeFlow S.L. (http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.addons.component.core import Component


class SaleService(Component):
    _inherit = "shopinvader.sale.service"
    _usage = "sales"

    def _convert_one_move(self, move):
        return {
            "quantity": move.product_qty,
            "product_id": move.product_id.id,
        }

    def _convert_moves(self, delivery):
        items = []
        for move in delivery.move_lines:
            items.append(self._convert_one_move(move))
        return items

    def _convert_one_delivery(self, delivery):
        res = super()._convert_one_delivery(delivery)
        res["lines"] = self._convert_moves(delivery)
        return res
