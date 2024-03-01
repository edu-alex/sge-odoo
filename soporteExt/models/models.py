# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class tecnico(models.Model):
    _name = 'soporte.tecnico'
    
    _inherit = ['soporte.tecnico','mail.thread']
    
    _description = 'Modelo para almacenar las personas que reparan incidencias'

    _rec_name= 'nombre'

    def name_get(self):
        result = []
        for record in self:
            valor = str(record.id)+'-'+str(record.nombre)+'_'+str(record.apellido1)
            result.append((record.id,valor))
        return result

    dni = fields.Char(
        string = 'DNI',
        size = 9,
        required = True
    )

    apellido1 = fields.Char(
        string = 'Primer apellido',
        required = True
    )
    apellido2 = fields.Char(
        string = 'Segundo apellido',
        required = True
    )
    
    fecha_nacimiento = fields.Date(
        string='Fecha de nacimiento',
    )
    
    fecha_incorporacion = fields.Date(
        string='Fecha incorporación',
        #default=fields.Date.context_today,
        default = lambda self: fields.Datetime.now(),
        readonly = True
    )
    
    foto = fields.Image(
        string = 'Foto',
        max_width=200,
        max_height=200
    )
    

    tipo = fields.Selection(
        string='Tipo',
        selection=[('0', 'Téc.general'), ('1', 'Téc.Hardware'), ('2', 'Téc.Software'), ('3', 'Téc.Redes')]
    )
    
    # Expresiones regulares: https://docs.python.org/es/3/library/re.html
    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('[0-9]{8}[A-Z]\Z',re.I)
        for record in self:
            if not regex.match(record.dni):
                raise ValidationError('Error. Formato DNI incorrecto.')
            
    
    
    _sql_constraints = [
        (
            'DNI_unico',
            'UNIQUE(dni)',
            ('El DNI debe ser único.')
        )
    ]
    
class incidencia(models.Model):
    _name = 'soporte.incidencia'
    _inherit = ['soporte.incidencia']
    _rec_name = 'id'

    

    
