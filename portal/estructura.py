from AccessControl.unauthorized import Unauthorized
import transaction
#import zope.app
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.unauthorized  import Unauthorized
from Testing import makerequest
#from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
#from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFPlone.utils import _createObjectByType



children_graduados = [{'id':'agricola',
                       'title':'Ingenieria Agricola',
                       'descripcion':'Registro de la carrera Ingenieria agricola',
                       'type':'Folder'},
                      {'id':'civi',
                       'title':'Ingenieria Civil',
                       'descripcion':'Registro de la carrera de Ingenieria Civil',
                       'type':'Folder'},
                      {'id':'mecanica',
                       'title':'Ingenieria Mecanica',
                       'descripcion':'Registro de la carrera de Ingenieria Mecanica',
                       'type':'Folder'},
                      {'id':'industrial',
                       'title':'Ingenieria Industrial',
                       'descripcion':'Registro de la carrera de Ingenieria Industrial',
                       'type':'Folder'},
                      {'id':'arquitectura',
                       'title':'Arquitectura',
                       'descripcion':'Registro de la carrera de Arquitectura',
                       'type':'Folder'},
                      {'id':'quimica',
                       'title':'Ingenieria Quimica',
                       'descripcion':'Registro de la carrera de Ingenieria Quimica',
                       'type':'Folder'},
                      {'id':'electrica',
                       'title':'Ingenieria Electrica',
                       'descripcion':'Registro de la carrera de Ingenieria Electrica',
                       'type':'Folder'},
                      {'id':'electronica',
                       'title':'Ingenieria Electronica',
                       'descripcion':'Registro de la carrera de Ingenieria Electronica',
                       'type':'Folder'},
                      {'id':'computacion',
                       'title':'Ingenieria en Computacion',
                       'descripcion':'REgistro de la carrera de Ingenieria en Computacion',
                       'type':'Folder'},
                      {'id':'sistemas',
                       'title':'Ingenieria en Sistemas',
                       'descripcion':'Registro de la carrera de Ingenieria en Sistemas',
                       'type':'Folder'}]

carpetas = [{'id':'empresas',
             'title':'Empresas',
             'descripcion':'Carpetas de las empresas',
             'type':'Folder'},
            {'id':'graduados',
             'title':'Graduados',
             'descripcion':'Informacion de Graduados',
             'type':'Folder'},
            {'id':'blogs',
             'title':'Blogs del portal',
             'descripcion':'Blogs de participacion',
             'type':'Folder'},
            {'id':'ecuestas',
             'title':'Encuestas del Portal',
             'descripcion':'Encuetas del portal',
             'type':'Folder'},
            {'id':'comentarios',
             'descripcion':'Comentarios',
             'type':'Folder',
             'title':'Comentarios del Portal'},
            {'id':'bolsa-de-trabajo',
             'title':'Bolsa de Trabajo',
             'descripcion':'Bolsa de trabajo de la universidad nacional de Ingenieria',
             'type':'Folder'},
            {'id':'actividades',
             'title':'Actividades',
             'descripcion':'Las actividades que realiza la Direccion de extensiones y Vicerectoria',
             'type':'Folder'},
            {'id':'capacitaciones',
             'title':'Capacitaciones Solicitadas',
             'descripcion':'Las capacitaciones solicitadas por parte de graduados y empresas',
             'type':'Folder'},
            {'id':'noticias',
             'title':'Noticias ',
             'descripcion':'Noticias Direccion de Extensiones de la UNI',
             'type':'Folder'}]

eliminar = ['news','events','front-page']

app = makerequest.makerequest(app)
sitios = app.objectValues('Plone Site')


context=app.deu

# usamos el usuario administrador del portal
admin=app.acl_users.getUserById("portal")
newSecurityManager(None, admin)

for sitio in sitios:
        sitioId = sitio.id
        print sitioId
        if(sitioId == 'deu'):
            existing = sitio.objectIds('ATFolder')
            #sitio.loginAsPortalOnwer()
            wtool = getToolByName(sitio,'portal_workflow')
            for carpeta in carpetas:
                if carpeta['id'] in existing:
                    print 'ya existe la carpeta %s' %carpeta['id']
                else:
                    try:
                        sitio.invokeFactory(type_name=carpeta['type'],
                                      id=carpeta['id'],
                                      title=carpeta['title'],
                                      description=carpeta['descripcion'],
                                      )
                        transaction.commit()
                        print '\nLa carpeta %s se ha creado' %carpeta['id']
                        objeto = getattr(sitio,carpeta['id'])
                        objeto.reindexObject()

                        try:
                                if wtool.getInfoFor(objeto,'review_state') != 'published':
                                    wtool.doActionFor(objeto,'publish',comment='Publicando objeto...')
                                    print 'se ha publicado el contenido %s' %objeto
                                    objeto.reindexObject()
                        except WorkflowException:
                                    print 'no se ha publicado el contenido'
                        transaction.commit()
                    except Unauthorized:
                        print "El usuario Portal no tiene permiso para crear la carpeta %s" % carpeta

            #eliminar los objetos definidos en la lista eliminar
            print '\nEliminando Objetos'
            for item in eliminar:
                if item in existing:
                    sitio.manage_delObjects(item)
                    print 'Se ha eliminado el objeto %s' %item
                else:
                    print 'No se ha encontrado el objeto %s' %item
                transaction.commit()
            transaction.commit()
