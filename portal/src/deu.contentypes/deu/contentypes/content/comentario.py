# To change this template, choose Tools | Templates
# and open the template in the editor.
from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from deu.contentypes import contentypesMessageFactory as _

from deu.contentypes.interfaces import IComment
from deu.contentypes.config import PROJECTNAME

ComentarioSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
        atapi.TextField('description',
                           searcheable=1,
                           isMetadata=0,
                           required=1,
                           validators=('isTidyHtmlWithCleanup',),
                           widget=atapi.TextAreaWidget(label='Comentario',
                                               maxlength=1000,
                                               size=30,
                                               description='Agregue su comentario'))

))
schemata.finalizeATCTSchema(ComentarioSchema, moveDiscussion=False)

class Comentario(base.ATCTContent):
    implements(IComment)
    meta_type='Comentario'
    _at_rename_after_creation = True
    schema = ComentarioSchema

atapi.registerType(Comentario,PROJECTNAME)


