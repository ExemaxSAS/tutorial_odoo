# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TutorialOdoo(models.Model):
    _inherit = "sale.order"

    test_bool = fields.Boolean('Test Bool')
    test_int = fields.Integer('Test Int')
    test_float = fields.Float('Test Float')
    test_char = fields.Char('Test Char')
    test_text = fields.Text('Test Text')
    test_selection = fields.Selection([('type1', 'Tipo 1'),('type2', 'Tipo 2')], 'Test Selection')