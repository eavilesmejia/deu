"""Definition of the Solicitud de Personal content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from deu.contentypes import contentypesMessageFactory as _

from deu.contentypes.interfaces import ISolicituddePersonal
from deu.contentypes.config import PROJECTNAME

SolicituddePersonalSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField('puesto',
                      searchable=1,
                      isMetadata=0,
                      required=True,
                      widget=atapi.StringWidget(label='Puesto Ofrecido',
                                                maxlength=150,
                                                size=30,
                                                label_msgid='lable_entry_puesto',
                                                description_msgid='help_entry_puesto',
                                                i18n_domain='deu.contentypes',
                                                description='Puesto Ofrecido'
                      )
    ),
    atapi.StringField('plazas',
                      searchable=True,
                      isMetadata=False,
                      required=True,
                      widget=atapi.StringWidget(label='Numero de Plazas',
                                                maxlength=10,
                                                size=15,
                                                label_msgid='lable_entry_plazas',
                                                description_msgid='help_entry_plazas',
                                                i18n_domain='deu.contentypes',
                                                description='Numeros de Plazas'
    
                    )
    ),
  
    atapi.StringField('tipo',
                      searchable=True,
                      isMetadata=True,
                      required=True,
                      widget=atapi.SelectionWidget(fomat='radio',
                                                   label='Tipo',
                                                   label_msgid='label_help_tipo',
                                                   description_msgid='label_help_tipo',
                                                   description='Escoja el tipo de contrato'
                    ),
                    vocabulary=['Contrato Fijo',
                                'Contrato Temporal',
                                'Pasantia']
    ),

    atapi.DateTimeField('fecha',
                searchable=0,
                required=0,
                widget=atapi.CalendarWidget(label='Fecha Inicial de Entrevista',
                                      label_msgid="label_entry_fecha",
                                      show_hm = False,
                                      description_msgid="help_entry_fecha",
                                      i18n_domain="deu.contentypes",
                                      description='Fecha Inicial para las Entrevistas')),
                                      
    atapi.DateTimeField('fechafin',
                searchable=0,
                required=0,
                widget=atapi.CalendarWidget(label='Fecha Final de Entrevista',
                                      label_msgid="label_entry_fecha",
                                      show_hm = False,
                                      description_msgid="help_entry_fecha",
                                      i18n_domain="deu.contentypes",
                                      description='Fecha Final para las Entrevistas')),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.
#
SolicituddePersonalSchema['title'].storage = atapi.AnnotationStorage()
#SolicituddePersonalSchema['title'].widget.label = _(u"Puesto Ofrecido")
#SolicituddePersonalSchema['title'].widget.description = _(u"Puesto Ofrecido")
#
SolicituddePersonalSchema['description'].storage = atapi.AnnotationStorage()
#SolicituddePersonalSchema['description'].widget.label = _(u"Plazas")
#SolicituddePersonalSchema['description'].widget.description = _(u"Numero de Plazas")

schemata.finalizeATCTSchema(SolicituddePersonalSchema, moveDiscussion=False)


class SolicituddePersonal(base.ATCTContent):
#class SolicituddePersonal(folder.ATFolder):
    """Description of the Example Type"""
    implements(ISolicituddePersonal)

    meta_type = "SolicituddePersonal"
    _at_rename_after_creation = True
    schema = SolicituddePersonalSchema

#    puesto = atapi.ATFieldProperty('title')
#    plazas = atapi.ATFieldProperty('description')
#    tipo = atapi.ATFieldProperty('tipo')
#    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(SolicituddePersonal, PROJECTNAME)
