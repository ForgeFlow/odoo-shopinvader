# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shopinvader Variant Attribute Image",
    "description": """
        This module adds the ability to add images to the attribute values""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "ForgeFlow S.L.",
    "website": "https://github.com/ForgeFlow/odoo-shopinvader",
    "depends": [
        "shopinvader_product_variant_selector",
        "shopinvader_image",
    ],
    "data": [
        "views/product_attribute_views.xml"
    ],
}
