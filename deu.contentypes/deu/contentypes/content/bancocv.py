"""Definition of the Solicitud de Personal content type
"""

from zope.interface import implements


from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from deu.contentypes import contentypesMessageFactory as _

from deu.contentypes.interfaces import ICurriculum
from deu.contentypes.config import PROJECTNAME


BancoDatosSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
        atapi.StringField('nombres',
                            searcheable=1,
                            isMetadata=0,
                            required=True,
                            storage=atapi.AnnotationStorage(),
                            widget=atapi.StringWidget(label=_(u"Nombres y Apellidos"),
                                                    maxlength=150,
                                                    label_msgid='lable_entry_nombres',
                                                    description_msgid='help_entry_nombres',
                                                    i18_domain='deu.contentypes',
                                                    description=_(u""))),


        atapi.StringField('carrera',
                          searcheable=1,
                          isMetadata=0,
                          required=1,
                          storage=atapi.AnnotationStorage(),
                          widget=atapi.SelectionWidget(fomat=_(u'radio'),
                                                       label=_(u"Carrera"),
                                                       maxlength=150,
                                                       i18_domain="deu.contentypes"),
                           vocabulary=[u'Ing.Civil',u'Ing.Agricola',u'Ing.Industrial',u'Ing.Mecanica',
                                       u'Arquitectura',u'Ing.Quimica',u'Ing.Electrica',u'Ing.Electronica',
                                       u'Ing.Computacion',u'Ing.Sistema',u'Ing.AgroIndustrial',u'Ing.Telecomunicacion']
                           ),
        atapi.StringField('email',
                          searcheable=1,
                          isMetadata=0,
                          required=1,
                          storage=atapi.AnnotationStorage(),
                          validators=('isEmail',),
                          widget=atapi.StringWidget(label=_(u"Email"),
                                                       maxlength=150,
                                                       i18_domain="deu.contentypes")
                           ),

       atapi.FileField('cv',
                          searcheable=1,
                          isMetadata=0,
                          required=1,
                          storage=atapi.AnnotationStorage(),
                          widget=atapi.FileWidget(label=_(u"Curriculum Vitae"),
                                                   maxlength=150,
                                                   i18_domain="deu.contentypes")
                       )

))

#ocultamos los campos titulo y descripcion que trae plone por defecto
BancoDatosSchema['title'].widget.visible = {"edit":"invisible"}
BancoDatosSchema['description'].widget.visible = {"edit":"invisible"}

schemata.finalizeATCTSchema(BancoDatosSchema, moveDiscussion=False)

class Curriculum(base.ATCTContent):
    """Campos para arquetipo Banco datos"""
    implements(ICurriculum)
    meta_type='Curriculum'
    schema = BancoDatosSchema

    _at_rename_after_creation = True
    
#registramos el arquetipo
atapi.registerType(Curriculum, PROJECTNAME)
