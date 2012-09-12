import re

from zope import interface, schema
from zope.formlib import form

from five.formlib.formbase import PageForm


from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot

from zope.app.form.interfaces import WidgetInputError, InputErrors

from zope.app.form.browser import TextWidget, CheckBoxWidget, ASCIIWidget
from ZODB.POSException import ConflictError

from Products.CMFPlone import PloneMessageFactory as _
from plone.app.users.userdataschema import IUserDataSchemaProvider

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.site.hooks import getSite
from plone.protect import CheckAuthenticator


class registroSchema(interface.Interface):

    nombre = schema.TextLine(title=_(u"Nombre de la Empresa"),
                             description=_(u"Nombre completeo de la Empresa"))

    username = schema.ASCIILine(
            title=_(u'Nombre de Usuario'),
            description=_(u"Ingrese el nombre de usuario, generalmente como \
                               Juan Perez. \
                               No use espacios ni caracteres especiales. \
                               Usernames and passwords are case sensiti."),
            required=True)
            
    telefono = schema.TextLine(title=_(u'Telefono'),
                                description=_(u'Telefono de la Empresa'),
                                required=True)

    email = schema.ASCIILine(
        title=_(u'Enter an email address'),
        description=_(u'Su correo Electronico'),
        required=True
        )


    direccion = schema.TextLine(title=_(u'Direccion'),
                                description=_(u'Introdusca la Direccion Fisica de su Empresa'),
                                required=False)

    descripcion = schema.SourceText(title=_(u"Perfil de la Empresa"),
                                     description=_(u"Agregue una breve descripcion"),
                                     required=False)

    password = schema.Password(
        title=_(u'Password'),
        description=_(u'Minimo 5 caracteres.'),
        required=True)


    password_ctl = schema.Password(
        title=_(u'Confirmar el Password'),
        description=_(u"Vuelva a Ingresar el password."),
        required=True)

    denominacion = schema.Choice(
            title=_(u'Denominacion'),
            values=[u'Publica',u'Privada'],
            default=u"Publica"
            )

class registroForm(PageForm):

#    render = ViewPageTemplateFile('registro_empresas.pt')
    
#    fields = field.Fields(registroSchema)
#    ignoreContext = True # don't use context to get widget data

    label = u"Registra tu empresa o Institucion"
    description = u""
    
    @property
    def form_fields(self):
        """ form_fields is dynamic in this form, to be able to handle
        different join styles.
        """
        portal_props = getToolByName(self.context, 'portal_properties')
        props = portal_props.site_properties
#        registration_fields = list(props.getProperty(
#                'user_registration_fields', []))
#
        registration_fields = ['nombre','username','telefono','email','direccion',
                                'descripcion','password',
                                'password_ctl','denominacion']

        # si no esta el campo en la lista, agregarlo
        if not 'nombre' in registration_fields:
            registration_fields.append('nombre')

        if not 'username' in registration_fields:
            registration_fields.append('username')

        if not 'telefono' in registration_fields:
            registration_fields.append('telefono')

        if not 'email' in registration_fields:
            registration_fields.append('email')

        if not 'direccion' in registration_fields:
            registration_fields.append('direccion')

        if not 'descripcion' in registration_fields:
            registration_fields.append('descripcion')

        if not 'denominacion' in registration_fields:
            registration_fields.append('denominacion')

        if not 'password' in registration_fields:
            if 'username' in registration_fields:
                base = registration_fields.index('username')
            else:
                base = registration_fields.index('email')
            registration_fields.insert(base + 1, 'password')

        # Add password_ctl after password
        if not 'password_ctl' in registration_fields:
            registration_fields.insert(
                registration_fields.index('password') + 1, 'password_ctl')

        # We need fields from both schemata here.
        util = getUtility(IUserDataSchemaProvider)
        schema = util.getSchema()

        all_fields = form.Fields(registroSchema)

        # Make sure some fields are really required; a previous call
        # might have changed the default.
        for name in ('password', 'password_ctl'):
            all_fields[name].field.required = True

        # Pass the list of join form fields as a reference to the
        # Fields constructor, and return.
        return form.Fields(*[all_fields[id] for id in registration_fields])

    def validacion(self,action,data):
        # CSRF protection
        CheckAuthenticator(self.request)
        registration = getToolByName(self.context, 'portal_registration')
        portal_props = getToolByName(self.context, 'portal_properties')
        props = portal_props.site_properties
        portal = getUtility(ISiteRoot)

        errors = super(registroForm, self).validate(action, data)
        # ConversionErrors have no field_name attribute... :-(
        error_keys = [error.field_name for error in errors
                      if hasattr(error, 'field_name')]

        form_field_names = [f.field.getName() for f in self.form_fields]
        
        #validar username e email
        username = ''
        email = ''
        try:
            email = self.widgets['email'].getInputValue()
        except InputErrors, exc:
            # WrongType?
            errors.append(exc)
        
        username_field = 'username'
        try:
            username = self.widgets['username'].getInputValue()
        except InputErrors, exc:
            errors.append(exc)

        #check characters especial
#        if not username_field in error_keys:
#            chek = re.match('[a-zA-Z0-9\.\_\]+', username)
#            if not chek.groups():
#                err_str = _(u"Nombre de Usuario no es Valido, por favor escoja otro")
#                errors.apend(WidgetInputError(
#                            username_field,u'labler_username',errstr))
#                self.widgets[username_field].error = err_str
            
        # check if username is valid
        # Skip this check if username was already in error list
        if not username_field in error_keys:
            if username == portal.getId():
                err_str = _(u"Este username es reservado. Porfavor escoja "
                            "uno diferente.")
                errors.append(WidgetInputError(
                        username_field, u'label_username', err_str))
                self.widgets[username_field].error = err_str


        # check if username is allowed
        if not username_field in error_keys:
            if not registration.isMemberIdAllowed(username):
                err_str = _(u"el nombre del usuario ya existe "
                            "o no es valido, porfavor escoja otro.")
                errors.append(WidgetInputError(
                        username_field, u'label_username', err_str))
                self.widgets[username_field].error = err_str


        # Skip this check if email was already in error list
        if not 'email' in error_keys:
            if 'email' in form_field_names:
                if not registration.isValidEmail(email):
                    err_str = _(u'debe ingresar un email valido.')
                    errors.append(WidgetInputError(
                            'email', u'label_email', err_str))
                    self.widgets['email'].error = err_str

        if 'password' in form_field_names:
            assert('password_ctl' in form_field_names)
            # Skip this check if password fields already have an error
            if not ('password' in error_keys or \
                    'password_ctl' in error_keys):
                password = self.widgets['password'].getInputValue()
                password_ctl = self.widgets['password_ctl'].getInputValue()

                # passwords should match
                if password != password_ctl:
                    err_str = _(u'Passwords do not match.')
                    errors.append(WidgetInputError('password',
                                  u'label_password', err_str))
                    errors.append(WidgetInputError('password_ctl',
                                  u'label_password', err_str))
                    self.widgets['password'].error = err_str
                    self.widgets['password_ctl'].error = err_str


        # Password field should have a minimum length of 5
        if 'password' in form_field_names:
            # Skip this check if password fields already have an error
            if not 'password' in error_keys:
                password = self.widgets['password'].getInputValue()
                if password and len(password) < 5:
                    err_str = _(u'Passwords must contain at least 5 letters.')
                    errors.append(WidgetInputError(
                            'password', u'label_password', err_str))
                    self.widgets['password'].error = err_str

        
        return errors

#    @button.buttonAndHandler(_(u'Guardar'),validator='validacion',name=u'guardar')
    @form.action(_(u'Registrar'),validator='validacion',name=u'registro')
    def handleApply(self, action,data):
        self.handle_join_success(data)
        return self.context.unrestrictedTraverse('registered')()


    def handle_join_success(self, data):
        portal = getUtility(ISiteRoot)
        registration = getToolByName(self.context, 'portal_registration')
        portal_props = getToolByName(self.context, 'portal_properties')
        props = portal_props.site_properties


        username = data['username']
        password = data.get('password') or registration.generatePassword()

        try:
            registration.addMember(username, password, properties=data,
                                   REQUEST=self.request)
        except (AttributeError, ValueError), err:
            IStatusMessage(self.request).addStatusMessage(err, type="error")
            return

        return
#RegistroView = wrap_form(registroForm)
