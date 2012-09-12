try:
    from Products.validation.interfaces.IValidator import IValidator
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
    from interfaces.IValidator import IValidator
    del sys, os

class AnonValidator:
    __implements__ = IValidator

    def __init__(self,
                 name,
                 title='Validador',
                 description='Pregunta de seguridad'):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):
        if value == "Managua" or value == "managua":
            print "Correcto"
            return 1
        else:
            return('Respuesta incorrecto')

"""try:
    from Products.validation.interfaces.IValidator import IValidator
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
    from interfaces.IValidator import IValidator
    del sys, os

class EvilValidator:
    __implements__ = IValidator

    def __init__(self, name, title='Validator', description='You will fail'):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):
        if value = "Managua":
            return 1
        else:
            return('Moahahahaha - you FAIL!')"""
