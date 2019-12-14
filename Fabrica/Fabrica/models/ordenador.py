from odoo import models, fields, api

class Ordenador(models.Model):
    _name = 'fabrica.ordenador'
    codigo = fields.Integer('Codigo de identificacion', required = True)
    modelo = fields.Char('Modelo', required = True)
    precio = fields.Float('Precio', required = True)
    codProcesador = fields.Many2one('fabrica.procesador', 'Codigo Procesador')
    codPlacaBase = fields.Many2one('fabrica.placa', 'Codigo Placa Base')