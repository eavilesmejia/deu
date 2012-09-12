from zope.interface import Interface
from zope import schema
from zope.app.container.constraints import contains
from deu.contentypes import contentypesMessageFactory as _

from plone.theme.interfaces import IDefaultPloneLayer

class ISolicituddePersonal(Interface):
    """a SolicituddePersonal"""

class ICurriculum(Interface):
    """Interface para el arquetipo Banco curriculum"""
#    nombres = schema.TextLine(title=_(u"Nombres"),
#                            description=_(u"Sus dos Nombres")
#                            )
#
#    apellidos = schema.TextLine(title=_(u"Apellidos"))
#
#    nacionalidad = schema.List(
#        value_type=schema.TextLine(
#            title=u"Nacionalidad",
#            default=u"Seleccione",
#            required=False,
#        ),
#        default=[u'Nicaraguense',u'Otra'],
#    )
#
#    departamento = schema.List(
#        value_type=schema.TextLine(
#            title=u"Departamento",
#            default=u"Seleccione"
#        ),
#        default=[u'Boaco',u'Carazo',u'Chinandega',u'Chontales',
#                 u'Esteli',u'Granada',u'Jinotega',u'Leon',u'Madriz',
#                 u'Managua',u'Masaya',u'Matagalpa',u'Nueva Segovia',u'Region Autonoma del Atlantico Norte',
#                 u'Region Autonoma del Atlantico Sur',u'Rio San Juan',u'Rivas']
#    )
#
#    email = schema.TextLine(title=u"Author", required=False)
#
#    carrera = schema.List(
#        value_type=schema.TextLine(
#            title=u"Carrea",
#            default=u"seleccione",
#        ),
#        default=[u'Ing.Civil',u'Ing.Agricola',u'Ing.Industrial']
#    )
#
#    telefono = schema.TextLine(title=u"Telefono",required=False)
#
#    celular = schema.TextLine(title=u"Celular",required=False)

class IComment(Interface):
    """clase Interface para el arquetipo solicitud capacitacion"""


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Skin para Direccion de Extensiones UNI" theme, this interface must be its layer
       (in deu/viewlets/configure.zcml).
    """
