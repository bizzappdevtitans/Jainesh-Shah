# -*- coding: utf-8 -*-
{
    "name": "validate_vendor",
    "summary": """
        Check for vendor pricelist""",
    "description": """
        this will raise validation error if vendor has issued same pricelist on same
        product with same date range and quantity
    """,
    "author": "Bizzappdev",
    "website": "http://www.bizzappdev.com",
    "category": "Purchase",
    "version": "15.0.0.0.1",
    "depends": [
        "base",
        "sale",
        "sale_management",
        "stock",
        "purchase",
        "account",
        "product",
    ],
    "license": "LGPL-3",
}
