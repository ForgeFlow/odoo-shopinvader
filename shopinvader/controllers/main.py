# Copyright 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# Copyright 2019 Camptocamp (http://www.camptocamp.com)
# Simone Orsi <simone.orsi@camptocamp.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import _
from odoo.addons.base_rest.controllers import main
from odoo.exceptions import MissingError
from odoo.http import request, route

_logger = logging.getLogger(__name__)


class InvaderController(main.RestController):

    _root_path = "/shopinvader/"
    _collection_name = "shopinvader.backend"
    _default_auth = "api_key"

    @route(["/shopinvader/invoice/<int:_id>/download"], methods=["GET"])
    def invoice_download(self, _id=None, **params):
        params["id"] = _id
        return self._process_method(
            "invoice", "download", _id=_id, params=params
        )

    @classmethod
    def _get_partner_from_headers(cls, headers):
        partner_model = request.env["shopinvader.partner"]
        partner_email = headers.get("HTTP_PARTNER_EMAIL")
        backend = cls._get_shopinvader_backend_from_request()
        if partner_email:
            partner = cls._find_partner(backend, partner_email)
            if len(partner) == 1:
                cls._validate_partner(backend, partner)
                return partner.record_id
            else:
                _logger.warning("Wrong HTTP_PARTNER_EMAIL, header ignored")
                if len(partner) > 1:
                    _logger.warning(
                        "More than one shopinvader.partner found for:"
                        " backend_id={} email={}".format(
                            backend.id, partner_email
                        )
                    )
                # Could be because the email is not related to a partner or
                # because the partner is inactive
                raise MissingError(_("The given partner is not found!"))
        return partner_model.browse([]).record_id

    @classmethod
    def _find_partner(cls, backend, partner_email):
        partner_domain = [
            ("partner_email", "=", partner_email),
            ("backend_id", "=", backend.id),
        ]
        return request.env["shopinvader.partner"].search(
            partner_domain, limit=2
        )

    @classmethod
    def _validate_partner(cls, backend, partner):
        with backend.work_on("res.partner") as work:
            validator = work.component(usage="partner.validator")
            validator.validate_partner(partner)

    @classmethod
    def _get_shopinvader_backend_from_request(cls):
        backend_model = request.env["shopinvader.backend"]
        return backend_model._get_from_http_request()

    @classmethod
    def _get_shopinvader_session_from_headers(cls, headers):
        # HTTP_SESS are data that are store in the shopinvader session
        # and forwarded to odoo at each request
        # it allow to access to some specific field of the user session
        # By security always force typing
        # Note: rails cookies store session are serveless ;)
        return {"cart_id": int(headers.get("HTTP_SESS_CART_ID", 0))}

    def _get_component_context(self):
        """
        This method adds the component context:
        * the partner
        * the cart_id
        * the shopinvader_backend
        """
        res = super(InvaderController, self)._get_component_context()
        headers = request.httprequest.environ
        res["partner"] = self._get_partner_from_headers(headers)
        # allow having a different partner for the user in extending modules
        res["partner_user"] = res["partner"]
        res[
            "shopinvader_session"
        ] = self._get_shopinvader_session_from_headers(headers)
        res[
            "shopinvader_backend"
        ] = self._get_shopinvader_backend_from_request()
        return res
