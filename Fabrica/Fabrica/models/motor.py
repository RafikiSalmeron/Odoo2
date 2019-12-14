from odoo import models, fields, api

class Motor(models.Model):
    _name = 'fabrica.motor'
    codigo = fields.Char('Codigo de identificacion', required=True)
    marca = fields.Char('Marca', required=True)
    potencia = fields.Integer('Potencia', required=True)
    tipo = fields.Char('Tipo de Combustible', required=True)

    def name_get(self):
        res = []

        for record in self:
            name = record.potencia
            res.append((record.id, name))
        return res