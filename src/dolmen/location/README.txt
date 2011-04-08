dolmen.location
***************

  >>> import dolmen.location
  >>> import grokcore.component
  >>> grokcore.component.testing.grok('dolmen.location')


URL
===

Scenario
--------

  >>> from cromlech.webob.request import Request
  >>> request = Request.blank('/somepath')

For a simple scenario : /obj:grandfather/obj:father/obj:me

  >>> from zope.location import Location
  >>> grandfather = Location()
  >>> father = Location()
  >>> me = Location()

  >>> me.__parent__ = father
  >>> me.__name__ = 'Grok'

  >>> father.__parent__ = grandfather
  >>> father.__name__ = 'Krao'

  >>> grandfather.__name__ = 'Ghran'


Without clear publication root
------------------------------

  >>> print dolmen.location.get_absolute_url(me, request)
  Traceback (most recent call last):
  ...
  LookupError: The path of the application root could not be resolved.


With a defined publication root
-------------------------------

  >>> from cromlech.io import IPublicationRoot
  >>> from zope.interface import directlyProvides
  >>> directlyProvides(grandfather, IPublicationRoot)

  >>> print dolmen.location.get_absolute_url(me, request)
  http://localhost/Krao/Grok

  >>> print dolmen.location.get_relative_url(me, request)
  /Krao/Grok
