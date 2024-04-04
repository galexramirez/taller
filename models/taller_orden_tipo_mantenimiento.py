# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class OrdenTipoMantenimiento(models.Model):
    _name = "taller.orden.tipo.mantenimiento"
    _description = "Tipo de Mantenimiento"
    
    name = fields.Char(string="Tipo de Mantenimiento", required=True)