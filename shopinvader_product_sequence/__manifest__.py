# Copyright 2021 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Shopinvader Product Sequence",
    "summary": "Add a sequence to shopinvader variant products",
    "version": "13.0.1.0.0",
    "category": "e-commerce",
    "website": "https://github.com/shopinvader/odoo-shopinvader",
    "author": "ForgeFlow",
    "license": "AGPL-3",
    "installable": True,
    "data": [
        "data/ir_export_product.xml",
        "views/shopinvader_variant_view.xml",
    ],
    "depends": ["shopinvader"],
}
