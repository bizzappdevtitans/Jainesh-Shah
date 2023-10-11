# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import ValidationError


class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    @api.constrains("name", "min_qty", "date_start", "date_end", "product_tmpl_id")
    def _check_another_vendor_pricelist(self):
        """This function will check for if same pricelist is present with same vendor,
        same quantity,same range of time and for same product then it will raise an
        validation error
        the code line id != self.id is written because while updating vendor pricelist
        from page vendor in product template validation can occur
        T00461"""
        record = self.env["product.supplierinfo"].search(
            [
                ("name", "=", self.name.id),
                ("min_qty", "=", self.min_qty),
                ("date_start", "=", self.date_start),
                ("date_end", "=", self.date_end),
                ("product_tmpl_id", "=", self.product_tmpl_id.id),
                ("id", "!=", self.id),
            ]
        )
        if record:
            raise ValidationError(
                _(
                    "Vendor Price List Already Present with\n"
                    + "Same Vendor\nSame Quantity\nSame Validate time range\nsame product"
                )
            )
