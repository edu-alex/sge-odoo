# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class incidencia(models.Model):
    _name = 'soporte.incidencia'
    _description = 'Modelo para la gestión de incidencias'
    
    def informe_incidencia_boton(self):
        return self.env.ref('soporte.action_informe_incidencia').report_action(self)
    
    titulo = fields.Char(
        string='Titulo',
        required=True,
        default='Incidencia X'   
    )
    descripcion = fields.Html(
        string='Descripcion',
        help='Explicación de la incidencia ocurrida brevemente.', 
        required = True
    )
    prioridad = fields.Integer(
        string='Prioridad',
            
        help='Establezca un valor entre 0 y 10. Si el valor es mayor de 7 será considerado urgente'
    )
    urgente = fields.Boolean(
        string='Urgente',
        compute='_compute_urgente',
        store = True
    )
        
    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            if record.prioridad > 7:
                record.urgente = True
            else:
                record.urgente = False
    
    @api.constrains('prioridad')
    def _check_prioridad(self):
        for record in self:
            if record.prioridad > 10:
                raise ValidationError("Error en prioridad. Debe introducir un valor menor o igual a 10.")
    '''
    ubicacion = fields.Selection(
        string='Ubicación',
        selection=[('1', 'Aula1'), ('2', 'Aula2')]
    )
    ''' 
    ubicacion_id = fields.Many2one(
        string='Ubicación',
        comodel_name='soporte.ubicacion',
        ondelete='restrict',
    )
    
    cerrada = fields.Boolean(
        string='Cerrada',
        default=False
    )

    
    archivo = fields.Binary(
        string='Archivo adjunto',
    )
    foto = fields.Image(
        string='Foto',
        max_width=250,max_height=250
    )
    
    
    fecha_creacion = fields.Datetime(
        string='Fecha de creación',
        #Solo se ejecuta en el momento de la creación del modelo
        default=fields.Datetime.now(),
        
        readonly=True 
        
    )

    
    fecha_modificacion = fields.Datetime(
        string='Fecha de última modificación',
        #Se ejecuta en la creación de cada registro
        default=lambda self: fields.Datetime.now(),
        
        readonly=True 
        
    )
    
    @api.onchange('titulo','descripcion','prioridad','ubicacion_id','cerrada','archivo')
    def _onchange_fecha_modificacion(self):
        for record in self:
            record.fecha_modificacion = fields.Datetime.now()
    
    
    
    tecnico_ids = fields.Many2many('soporte.tecnico')
    
    
    _sql_constraints = [('intervalo_prioridad','CHECK (prioridad>=0 AND prioridad<11)','Prioridad entre 0 y 10')]
    
    
    
    
    
class ubicacion(models.Model):
    _name = 'soporte.ubicacion'
    _description = 'Modelo para almacenar ubicaciones'
    _rec_name= 'nombre'
    
        
    nombre = fields.Char(
        string='Nombre',
        required=True     
    )
    
    pabellon = fields.Selection(
        string='Pabellón',
        selection=[('1', 'Pabellón París'), ('2', 'Pabellón Roma')]
    )
    
    planta = fields.Selection(
        string='Planta',
        selection=[('0', 'Planta baja'),('1', 'Planta primera'), ('2', 'Planta segunda')]
    )
    
    incidencias_ids = fields.One2many('soporte.incidencia','ubicacion_id')
    

class tecnico(models.Model):
    _name = 'soporte.tecnico'
    _description = 'Modelo para almacenar las personas que reparan incidencias'

    _rec_name= 'nombre'

    nombre = fields.Char(
        string='Nombre',
        required=True
        
    )
    
    incidencia_ids = fields.Many2many('soporte.incidencia')
    
    
    

    

    
