from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName

from zope.app.component.hooks import getSite
from zope.component import getMultiAdapter
from AccessControl import getSecurityManager
from Products.PlonePopoll.browser import popoll

# Sample code for a basic viewlet (In order to use it, you'll have to):
# - Un-comment the following useable piece of code (viewlet python class).
# - Rename the viewlet template file ('browser/viewlet.pt') and edit the
#   following python code accordingly.
# - Edit the class and template to make them suit your needs.
# - Make sure your viewlet is correctly registered in 'browser/configure.zcml'.
# - If you need it to appear in a specific order inside its viewlet manager,
#   edit 'profiles/default/viewlets.xml' accordingly.
# - Restart Zope.
# - If you edited any file in 'profiles/default/', reinstall your package.
# - Once you're happy with your viewlet implementation, remove any related
#   (unwanted) inline documentation  ;-p


class pathBar(ViewletBase):
    render = ViewPageTemplateFile('templates/path.pt')
    
    def update(self):
        super(pathBar,self).update()
        self.is_rtl = self.portal_state.is_rtl()
        breadcrumbs_view = getMultiAdapter((self.context,self.request),
                                            name=u'breadcrumbs_view')
        self.breadcrumbs = breadcrumbs_view.breadcrumbs()

        portal = getSite()
        self.portalUrl = portal.absolute_url()
        
class footerView(ViewletBase):
    render = ViewPageTemplateFile('templates/footer.pt')
    
    def ultimosBlogs(self):
        miUtils = utils(self.context)
        catalog = miUtils.catalog
        result = catalog.searchResults(portal_type='Blog Entry',sort_on='Date',sort_order='descending',sort_limit=4)[:4]
        return result

    def encuestas(self):
        miUtils = utils(self.context)
        catalog = miUtils.catalog
        result = catalog.searchResults(portal_type='PlonePopoll',sort_on='Date',sort_order='desceding',sort_limit=4)[:4]
        return result

    def comentarios(self):
        miUtils = utils(self.context)
        catalog = miUtils.catalog
        result = catalog.searchResults(portal_type='Comentario',sort_on='Date',sort_order='descending',sort_limit=4)[:4]
        return result

class logoViewlet(ViewletBase):
    """logo viewlet"""
    render = ViewPageTemplateFile('templates/logo.pt')
    def update(self):
        super(logoViewlet, self).update()

        portal = self.portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        self.logo_tag = portal.restrictedTraverse(logoName).tag()

        self.portal_title = self.portal_state.portal_title()
        
class utils:
    def __init__(self,context):
        self.context = context
        self.catalog = getToolByName(self.context,'portal_catalog')
        self.portal = getSite()
        self.portal_url = self.portal.absolute_url()
