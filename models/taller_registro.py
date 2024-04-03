# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError

class Registro(models.Model):
    _name = "taller.registro"
    _description = "Taller Registro"
    
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    email = fields.Char(string="Email", required=True)