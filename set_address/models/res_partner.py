# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"
    # T00459 adding dropship type in address type and delivery boolean field
    type = fields.Selection(selection_add=[("dropship", "Drop Ship Address")])
    delivery = fields.Boolean(string="set delivery address")
