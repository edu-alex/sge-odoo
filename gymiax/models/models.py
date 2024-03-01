# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = 'gymiax.profesor'
    _description = 'Modelo para profesor del gimnasio'

    
    nombre = fields.Char(
        string='Nombre', 
        required=True
    )
    apellido1 = fields.Char(
        string='Primer apellido', 
        required=True
    )
    apellido2 = fields.Char(
        string='Segundo apellido', 
        required=True
    )

class alumno(models.Model):
    _name = 'gymiax.alumno'
    _description = 'Modelo para alumnos del gimnasio'

    nre = fields.Char(
        string='Número Registro', 
        size=6,
        required=True,
    )
    nombre = fields.Char(
        string='Nombre', 
        required=True
    )
    apellido1 = fields.Char(
        string='Primer apellido', 
        required=True
    )
    apellido2 = fields.Char(
        string='Segundo apellido', 
        required=True
    )  


