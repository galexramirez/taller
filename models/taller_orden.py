# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError

class Orden(models.Model):
    _name = "taller.orden"
    _description = "Orden de Reparación"
    
    fecha_apertura = fields.Datetime(string="Fecha y Hora de Apertura", required=True)
    duracion = fields.Datetime(string="Duración", required=True)
    tipo_servicio_id = fields.Many2one("taller.orden.tipo.servicio", string="Tipo de Servicio", required=True)
    tipo_mantenimiento_id = fields.Many2one("taller.orden.tipo.mantenimiento", string="Tipo de Mantenimiento")
    cliente = fields.Many2one("res.partner", string="Cliente", required=True)
    conductor = fields.Many2one("res.partner", string="Conductor", required=True)
    celular = fields.Char(string="Celular")
    vehiculo_id = fields.Many2one("taller.orden.vehiculo", string="Vehículo", required=True)
    responsable_id = fields.Many2one("res.users", string="Responsable", readonly=True, index=True, tracking=True, default=lambda self: self.env.user)
    tecnico_id = fields.Many2one("res.users", string="Técnico Asignado", required=True)
    asistente_id = fields.Many2one("res.users", string="Asistente Lavado Asignado", required=True)
    sintomas = fields.Char(string="Sintomas")
    prueba_manejo = fields.Boolean(string="Prueba de Manejo")
    fecha_cierre = fields.Datetime(string="Fecha y Hora de Cierre")
    estado = fields.Selection(string="Estado", selection=[('en cotizacion', 'En Cotizacion'), ('cierre', 'Cierre'), ('check-in','Check-In'), ('check-in','Check-In')], default="en cotizacion")
    
