# To change this template, choose Tools | Templates
# and open the template in the editor.

from zope.interface import implements
from zope.interface import Interface

from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.formlib import form


#la interfaz solo la ocupamos por convencion, actualmente no hace nada
#mas que para rellenar elementos en configure.zcml
class IPortletBanco(IPortletDataProvider):
    """Esta clase tiene los campos del
    portlet usando schema
    Ejemplo:
    titulo = schema.TextLine(title=_(u"Titulo"),
                             description=_(u"Titulo de la cabezera del portlet"),
                             required=1)
    """
class Assignment(base.Assignment):
    """Esta clase implementa los campos
    definidos en IPortletComentario y los asigna
    al portlet"""
    implements(IPortletBanco)
    def __init__(self):
        pass

    @property
    def title(self):
        return "Banco de Curriculum"


class Renderer(base.Renderer):
    """Renderiza con una vista, la que
    mostrara el contenido del portlet en
    el portal"""
    render = ViewPageTemplateFile('banco.pt')

    def prueba(self):
        return 'Banco de Curriculum'

class AddForm(base.AddForm):
    """Este es registrado en configure.zcml
    la variable form_fields guarda los
    campos definido en IPortletBanco
    """
    form_fields = form.Fields(IPortletBanco)

    def create(self,data):
        """Llama a la clase Assignment para guardar
        los datos de los formularios
        Ejemplo:
            assignment = Assignment()
            form.appliyChanges(assigment, self.form_fields, data)
            return assignment
        """
        return Assignment(**data)

class EditForm(base.EditForm):
    """Edita los campos del portlet
    es configurado atravez de configure.zcml
    """
    form_fields = form.Fields(IPortletBanco)


