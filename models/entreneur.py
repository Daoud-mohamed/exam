from odoo import models, fields, api


class Entreneur(models.Model):
    _name = 'gestion_clubs.entreneur'
    _description = 'Model for entreneur'

    name = fields.Char('Nom')
    prenon = fields.Char('Prénom')
    tel = fields.Char('Tél')
    email = fields.Char('email')
    equipe = fields.One2many('gestion_clubs.equipe', 'entreneur_id')
