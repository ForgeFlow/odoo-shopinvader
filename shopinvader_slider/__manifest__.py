# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shopinvader Slider",
    "summary": """
        Add a way to store slides in Odoo""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "ForgeFlow S.L.",
    "website": "https://forgeflow.com",
    "depends": ["shopinvader_image"],
    "data": [
        "data/ir_product_export.xml",
        "views/product_template.xml",
        "security/shopinvader_slider.xml",
        "views/shopinvader_slider.xml",
        "views/shopinvader_slider_group_views.xml",
    ],
}
