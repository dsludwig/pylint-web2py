from logilab.astng import MANAGER
from logilab.astng.builder import ASTNGBuilder

def web2py_transform(module):
    if 'controllers' in module.name or 'views' in module.name:
        fake = ASTNGBuilder(MANAGER).string_build('''
from gluon.globals import *
from gluon.html import *
from gluon.http import *
from gluon.sqlhtml import SQLFORM, SQLTABLE, form_factory
session = Session()
request = Request()
response = Response()
''')
        module.locals.update(fake.locals)

def register(linter):
    MANAGER.register_transformer(web2py_transform)
