# Copyright 2021 ForgeFlow (http://www.forgeflow.com)
# @author Héctor Villarreal <hector.villarreal@forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=method-required-super

from odoo.addons.component.core import Component


class HelpdeskService(Component):
    """Shopinvader service to expose helpdesk.ticket features.
    """

    _inherit = "base.shopinvader.service"
    _name = "shopinvader.helpdesk.service"
    _usage = "helpdesk"
    _expose_model = "helpdesk.ticket"
    _description = __doc__

    # The following methods are 'public' and can be called from the controller.
    # All params are untrusted so please check it by using the decorator
    # secure params and the linked validator !

    def create(self, **params):
        vals = self._prepare_helpdesk_ticket(params)
        lead = self.env["helpdesk.ticket"].create(vals)
        self.shopinvader_backend._send_notification(
            "helpdesk_confirmation", lead
        )
        return {}

    # The following methods are 'private' and should be never NEVER be called
    # from the controller.
    # All params are trusted as they have been checked before

    def _validator_create(self):
        res = {
            "email": {"type": "string"},
            "name": {"type": "string", "required": True},
            "description": {"type": "string", "required": True},
        }
        return res

    def _prepare_helpdesk_ticket(self, params):
        map_key = [
            ("contact_name", "partner_name"),
            ("email", "partner_email"),
        ]
        for human_key, key in map_key:
            if human_key in params:
                params[key] = params.pop(human_key)
        params["shopinvader_backend_id"] = self.shopinvader_backend.id
        return params
