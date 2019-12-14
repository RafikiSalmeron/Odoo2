from odoo import models, fields, api

class Rueda(models.Model):
    _name = 'fabrica.rueda'
    codigo = fields.Char('Codigo de identificacion', required = True)
    marca = fields.Char('Marca', required = True)
    pulgadas = fields.Integer('Pulgadas', required = True)

    def name_get(self):
        res = []

        for record in self:
            name = record.marca
            res.append((record.id, name))
        return res