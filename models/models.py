# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TutorialOdoo(models.Model):
    _inherit = "sale.order"

    test_bool = fields.Boolean('Test')
    test_char = fields.Char('Test Char')