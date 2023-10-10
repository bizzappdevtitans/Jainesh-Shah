# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        """Inherited method from sale.order to update the partner_shipping_id
        if partner_id is company than check for employees which has address type
        delivery address and set delivery address is true.if we find more than one
        first employee must be selectef
        if condition is not fullfill
        again check for employees who has address type as dropship and if we get more
        than one then first employee is selected
        if no condition is fullfilled and than employees who address type is delivery
        is selected and from above all the condition non is selected than
        partner_shipping_id is company itself T00459"""

        self.ensure_one()
        super(SaleOrder, self).onchange_partner_id()
        partner = self.env["res.partner"].browse(self.partner_id.id)
        if not partner.is_company:
            return
        employees = partner.child_ids
        employee = employees.filtered(lambda x: (x.type == "delivery" and x.delivery))
        if not employee:
            employee = employees.filtered(lambda x: x.type == "dropship")
            if not employee:
                return
            employee = employee[:1]
            self.partner_shipping_id = employee
            return
        employee = employee[:1]
        self.partner_shipping_id = employee
