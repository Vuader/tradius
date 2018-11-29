
from luxon.utils.pkg import Module
from luxon.utils.files import rm
from luxon import register
from luxon import db
from luxon.helpers.rmq import rmq


@register.resource('subscribers', '/coa')
def coa(req, resp):
    pass
