# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class OrdenTipoServicio(models.Model):
    _name = "taller.orden.tipo.servicio"
    _description = "Tipo de Servicio"
    
    name = fields.Char(string="Tipo de Servicio", required=True)