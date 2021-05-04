# Copyright 2021 ForgeFlow (http://www.forgeflow.com)
# @author Héctor Villarreal <hector.villarreal@forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models

from odoo.addons.shopinvader.tests.common import CommonCase
from odoo.addons.shopinvader.tests.test_notification import (
    NotificationCaseMixin,
)


class HelpdeskCase(CommonCase, NotificationCaseMixin):
    def test_create_helpdesk_ticket(self):
        data = {
            "email": "revolution@shopinvader.com",
            "name": "Helpdesk Ticket",
            "contact_name": "A Customer",
            "description": "I had a problem with...",
        }
        check_data = data.copy()
        check_data.update(
            {
                "partner_email": check_data.pop("email"),
                "partner_name": check_data.pop("contact_name"),
            }
        )

        with self.work_on_services(
            partner=None, shopinvader_session=self.shopinvader_session
        ) as work:
            self.service = work.component(usage="helpdesk")
        self._init_job_counter()
        self.service.dispatch("create", params=data)
        helpdesk_ticket = self.env["helpdesk.ticket"].search(
            [], order="id desc", limit=1
        )[0]
        for key in check_data:
            if isinstance(helpdesk_ticket[key], models.Model):
                self.assertEqual(helpdesk_ticket[key].id, check_data[key])
            else:
                self.assertEqual(helpdesk_ticket[key], check_data[key])
        self._check_nbr_job_created(1)
        self._perform_created_job()

    def test_search_helpdesk_ticket(self):
        pass
