from odoo import models, fields, api

class Procesador(models.Model):
    _name = 'fabrica.procesador'
    codigo = fields.Char('Codigo de identificacion', required = True)
    marca = fields.Char('Marca', required = True)
    modelo = fields.Char('Modelo', required = True)

    def name_get(self):
        res = []

        for record in self:
            name = record.modelo
            res.append((record.id, name))
        return res