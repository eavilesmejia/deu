.. contents::

This is a simple widget and field for Archetypes that uses
collective.recaptcha to show a captcha in any archetypes-based content
type. Changes to the content type will not be saved if the captcha code
entered by the user is incorrect.

To use it, simple define a field in your archetypes schema that looks
like this example:

    RecaptchaedContentSchema = atapi.Schema((

        atapi.TextField(
            'Text',
            storage=atapi.AnnotationStorage(),
            widget=atapi.TextAreaWidget(
                label=_(u"Text"),
                description=_(u"Field description"),
            ),
            required=True,
        ),

        CaptchaField(
            'captcha',
        ),

    ))


- Code repository: http://svn.plone.org/svn/collective/collective.recaptchawidget
- Questions and comments to plone users list.

