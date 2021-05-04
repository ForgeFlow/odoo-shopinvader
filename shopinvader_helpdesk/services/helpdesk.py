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

    def search(self, **params):
        """
        Get every delivery related to logged user
        :param params: dict/json
        :return: dict
        """
        return self._paginate_search(**params)

    def create(self, **params):
        vals = self._prepare_helpdesk_ticket(params)
        ticket = self.env["helpdesk.ticket"].create(vals)
        self.shopinvader_backend._send_notification(
            "helpdesk_confirmation", ticket
        )
        return {}

    # The following methods are 'private' and should be never NEVER be called
    # from the controller.
    # All params are trusted as they have been checked before
    def _validator_search(self):
        """
        Validator for the search
        :return: dict
        """
        validator = self._default_validator_search()
        validator.pop("domain", {})
        validator.pop("scope", {})
        return validator

    def _validator_return_search(self):
        """
        Output validator for the search
        :return: dict
        """
        schema = {
            "size": {"type": "integer"},
            "data": {
                "type": "list",
                "schema": {
                    "type": "dict",
                    "schema": self._get_helpdesk_ticket_schema(),
                },
            },
        }
        return schema

    def _get_helpdesk_ticket_schema(self):
        """

        :return: dict
        """
        schema = {
            "ticket_id": {"type": "integer"},
            "name": {"type": "string", "nullable": True},
            "description": {"type": "string", "nullable": True},
            "partner_name": {"type": "string", "nullable": True},
            "partner_email": {"type": "string", "nullable": True},
            "team": {"type": "string", "nullable": True},
            "state": {"type": "string", "nullable": True},
            "create_date": {"type": "string", "nullable": True},
            "last_stage_update": {"type": "string", "nullable": True},
            "assigned_date": {"type": "string", "nullable": True},
            "closed_date": {"type": "string", "nullable": True},
        }
        return schema

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

    def _get_parser_helpdesk_ticket(self):
        """
        Get the parser of stock.picking
        :return: list
        """
        to_parse = [
            "name",
            "description",
            "partner_name",
            "partner_email",
            "create_date",
            "last_stage_update",
            "assigned_date",
            "closed_date",
            ("team_id:team", ("name",)),
            ("stage_id:state", ("name",)),
            "id:ticket_id",
        ]
        return to_parse

    def _to_json_helpdesk_ticket(self, ticket):
        ticket.ensure_one()
        parser = self._get_parser_helpdesk_ticket()
        values = ticket.jsonify(parser, one=True)
        return values

    def _to_json(self, tickets):
        res = []
        for ticket in tickets:
            res.append(self._to_json_helpdesk_ticket(ticket))
        return res
