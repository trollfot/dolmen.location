# -*- coding: utf-8 -*-

import urllib
from zope.location import ILocation
from zope.interface import Interface
from zope.component import getMultiAdapter

from cromlech.io.interfaces import IRequest, IPublicationRoot
from cromlech.browser.interfaces import IURLResolver


_safe = '@+'  # Characters that we don't want to have quoted

ABSOLUTE = u"absolute"
RELATIVE = u"relative"


def root_path(context, request, absolute=False):
    if IPublicationRoot.providedBy(context):
        return request.application_url if absolute is True else ''
    raise LookupError(
        'The path of the application root could not be resolved.')


def resolve_url(context, request, name):

    if context is None:
        return root_path(context, request, name==ABSOLUTE)
    
    # first try to get the __parent__ of the object, no matter whether
    # it provides ILocation or not. If this fails, look up an ILocation
    # adapter. This will always work, as a general ILocation adapter
    # is registered for interface in zope.location (a LocationProxy)
    # This proxy will return a parent of None, causing this to fail
    # More specific ILocation adapters can be provided however.
    try:
        container = context.__parent__
    except AttributeError:
        # we need to assign to context here so we can get
        # __name__ from it below
        context = ILocation(context)
        container = context.__parent__

    if container is None:
        return root_path(context, request, name==ABSOLUTE)
        
    url = getMultiAdapter((container, request), IURLResolver, name=name)

    name = getattr(context, '__name__', None)
    if name is None:
        raise KeyError(context, '__name__')

    if name:
        url += '/' + urllib.quote(name.encode('utf-8'), _safe)

    return url
    


def absolute_url(context, request):
    return resolve_url(context, request, name=ABSOLUTE)


def relative_url(context, request):
    return resolve_url(context, request, name=RELATIVE)


def get_absolute_url(context, request):
    return getMultiAdapter((context, request), IURLResolver, name=ABSOLUTE)
    

def get_relative_url(context, request):
    return getMultiAdapter((context, request), IURLResolver, name=RELATIVE)


try:
    from grokcore.component import global_adapter
    global_adapter(
        absolute_url, (Interface, IRequest), IURLResolver, name=ABSOLUTE)
    global_adapter(
        relative_url, (Interface, IRequest), IURLResolver, name=RELATIVE)
except ImportError:
    pass
