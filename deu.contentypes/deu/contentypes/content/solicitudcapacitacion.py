# To change this template, choose Tools | Templates
# and open the template in the editor.
from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from deu.contentypes import contentypesMessageFactory as _

from deu.contentypes.interfaces import ICapacitacion
from deu.contentypes.config import PROJECTNAME

SolicitudCapacitacionSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField('title',
                       searcheable=1,
                       isMetadata=0,
                       accesor='title',
                       required=True,
                       widget=atapi.StringWidget(label='Titulo',
                                                 maxlength=150,
                                                 description='Titulo de la capacitacion')),
    atapi.TextField('description',
                       searcheable=1,
                       isMetadata=0,
                       accesor='Description',
                       required=True,
                       widget=atapi.TextAreaWidget(label='Descripcion',
                                                 maxlength=300,
                                                 description='Mas detalle de la solicitud')),

))
SolicitudCapacitacionSchema['title'].storage = atapi.AnnotationStorage()
SolicitudCapacitacionSchema['description'].storage = atapi.AnnotationStorage()
schemata.finalizeATCTSchema(SolicitudCapacitacionSchema, moveDiscussion=False)


class SolicitudCapacitacion(base.ATCTContent):
    implements(ICapacitacion)
    meta_type='SolicitudCapacitacion'
    _at_rename_after_creation = True
    schema = SolicitudCapacitacionSchema

atapi.registerType(SolicitudCapacitacion,PROJECTNAME)