# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import ValidationError


class SupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    @api.constrains("name")
    def _check_another_vendor_pricelist(self):
        print("AAAA")
        print(self.name.id)
        print(self.min_qty)
        print(self.date_start)
        print(self.date_end)
        print(self.product_tmpl_id.id)
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
        print(record)
        if record:
            raise ValidationError(_("Vendor Price List Already Present"))
