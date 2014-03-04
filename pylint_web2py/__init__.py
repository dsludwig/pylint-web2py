from logilab.astng import MANAGER
from logilab.astng.builder import ASTNGBuilder

def web2py_transform(module):
    if 'controllers' in module.name or 'views' in module.name:
        # This dummy code is copied from gluon/__init__.py
        fake = ASTNGBuilder(MANAGER).string_build('''\
from gluon.globals import current
from gluon.html import *
from gluon.validators import *
from gluon.http import redirect, HTTP
from gluon.dal import DAL, Field
from gluon.sqlhtml import SQLFORM, SQLTABLE
from gluon.compileapp import LOAD

from gluon.globals import Request, Response, Session
from gluon.cache import Cache
from gluon.languages import translator
from gluon.tools import Auth, Crud, Mail, Service, PluginManager

# API objects
request = Request()
response = Response()
session = Session()
cache = Cache(request)
T = translator(request)

# Objects commonly defined in application model files
# (names are conventions only -- not part of API)
db = DAL()
auth = Auth(db)
crud = Crud(db)
mail = Mail()
service = Service()
plugins = PluginManager()
''')
        module.locals.update(fake.locals)



def register(linter):
    MANAGER.register_transformer(web2py_transform)
