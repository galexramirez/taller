# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class OrdenVehiculo(models.Model):
    _name = "taller.orden.vehiculo"
    _description = "Vehiculo"
    
    name = fields.Char(string="Placa", required=True)