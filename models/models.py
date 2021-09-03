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

    test_date = fields.Date('Test Date')
    test_html = fields.Html('Test HTML')
    test_binary = fields.Binary('Test Binary')

    test_many2one = fields.Many2one('res.partner', 'Test Many2one')
    test_one2many = fields.One2many(comodel_name='sale.order.tutorial', inverse_name='sale_order_id', string="Test One2Many")

class TutorialOdooLine(models.Model):
    _name = "sale.order.tutorial"

    name = fields.Char('Nombre')
    price = fields.Float('Precio')
    # Campos de Control
    sale_order_id = fields.Many2one('sale.order', 'Sale ID')