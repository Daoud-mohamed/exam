from odoo import models, fields, api
from datetime import datetime
from datetime import date
from dateutil import relativedelta
from odoo.exceptions import UserError, ValidationError


class Joueur(models.Model):
    _name = 'gestion_clubs.joueur'
    _description = 'Model for joueur'

    name = fields.Char('Nom')
    prenon = fields.Char('Prénom')
    tel = fields.Char('Tél')
    email = fields.Char('email')
    birthday = fields.Date('Date de naissance', default='2000-01-01')
    age = fields.Integer('Age', readonly="1" ,force_save="1")
    categorie = fields.Char('Catégorie', readonly="1" ,force_save="1")
    type = fields.Char('Type')
    position = fields.Selection([('dc','DC'),('md','MD'),('mo','MO'),('ac','AC')],'Position')
    note = fields.Char('note')
    entreneur = fields.Char('entreneur', readonly="1" ,force_save="1")

    equipe_id = fields.Many2one('gestion_clubs.equipe', string="Equipe")

    @api.onchange('birthday')
    def _onchange_age(self):
        today = date.today()
        for record in self:
            diff_dates = relativedelta.relativedelta(today, record.birthday)
            record.age = diff_dates.years

            if (record.age >= 16 and record.age < 18) :
                record.categorie = 'Cadet'
            elif (record.age >= 18 and record.age < 21):
                record.categorie = 'Junior'
            elif(record.age > 21):
                record.categorie = 'Senior'
            elif (record.age < 16):
                raise ValidationError('Age cant be less than 16.....')

    @api.onchange('equipe_id')
    def _onchange_entreneur(self):
        for record in self:
            record.entreneur = record.equipe_id.entreneur_id.name

