from odoo import models, fields, api


class Equipe(models.Model):
    _name = 'gestion_clubs.equipe'
    _description = 'Model for team'

    name = fields.Char('nomenclature')
    joueur = fields.One2many('gestion_clubs.joueur', 'equipe_id')
    entreneur_id = fields.Many2one('gestion_clubs.entreneur', string="Entreneur")

    _sql_constraints = [
        ('field_unique',
         'unique(name)',
         'Team name must be unique!..')
    ]
