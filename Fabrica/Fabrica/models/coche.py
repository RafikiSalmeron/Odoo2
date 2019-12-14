from odoo import models, fields, api

class Coche(models.Model):
    _name = 'fabrica.coche'
    bastidor = fields.Integer('Numero de Bastidor', required = True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required = True)
    precio = fields.Float('Precio', required = True)
    modeloRuedas = fields.Many2one('fabrica.rueda', 'Modelo Ruedas')
    codMotor = fields.Many2one('fabrica.motor', 'Codigo Motor')