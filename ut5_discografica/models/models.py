# -*- coding: utf-8 -*-

from odoo import models, fields


class discografica(models.Model):
    _name = 'discografica.disco'
    _description = 'discografica.disco'

    name = fields.Char(string='Título del disco',help='Título',required=True)
    year = fields.Char(string='Año',help='Año',size=4)
    genre = fields.Char(string='Género',help='Género')
    artist = fields.Char(string='Grupo/Banda',help='Grupo')
    cover = fields.Binary()
