# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):
    cr.execute(
        """
           ALTER TABLE shopinvader_product
           ADD COLUMN automatic_url_key character varying
       """
    )
