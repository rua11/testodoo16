# -*- coding: utf-8 -*-

from odoo import models, fields


class Test(models.Model):
    _name = 'testmodule'
    _description = 'demo'

    name = fields.Char(string="Ten")
    value2222222 = fields.Integer(string="Mot")
    value2 = fields.Float(compute="_value_pc", string="Hai", store=True)
    description = fields.Text(string="Chi iet")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
