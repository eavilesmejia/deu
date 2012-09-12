from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

class frontView(BrowserView):
    """ clase para el frontPage de la pagina"""
    template = ViewPageTemplateFile('templates/frontpage.html')
    def news(self):
        """retorna las ulitmas 4 noticias"""
        miutils = utils(self.context)
        catalog = miutils.catalog
        result = catalog.searchResults(portal_type='News Item', sort_on="Date",sort_order='descending',sort_limit=2)
        return result[0:2]

    def bolsa(self):
        """retorna las ultimas 4 solicitud de personal"""
        miutils = utils(self.context)
        catalog = miutils.catalog
        result = catalog.searchResults(portal_type="Solicitud de Personal", sort_on="Date",sort_order="descending",sort_limit=3)
        return result[0:3]
    
class utils:
    
    def __init__(self,context):
        self.context= context
        self.site = getSite()
        self.catalog = getToolByName(self.context,'portal_catalog')
        self.portalUrl = self.site.absolute_url()
