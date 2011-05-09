"""dolmen.location tests
"""
import pytest
import dolmen.location
import grokcore.component
from cromlech.io.testing import TestRequest
from zope.location import Location
from zope.testing.cleanup import cleanUp
from cromlech.io import IPublicationRoot
from zope.interface import directlyProvides


def setup_module(module):
    grokcore.component.testing.grok('dolmen.location')


def teardown_module(module):
    cleanUp()


def test_locatability():
    """For a simple scenario : /obj:grandfather/obj:father/obj:me
    """
    request = TestRequest(path='/somepath')
    grandfather = Location()
    father = Location()
    me = Location()

    me.__parent__ = father
    me.__name__ = 'Grok'

    father.__parent__ = grandfather
    father.__name__ = 'Krao'

    grandfather.__name__ = 'Ghran'

    with pytest.raises(LookupError) as e:
        """The Publication root is not defined
        """
        dolmen.location.get_absolute_url(me, request)

    assert str(e.value.message) == (
        "The path of the application root could not be resolved.")

    # We define a publication root.
    directlyProvides(grandfather, IPublicationRoot)
    assert dolmen.location.get_absolute_url(me, request) == (
        "http://localhost/Krao/Grok")

    assert dolmen.location.get_relative_url(me, request) == "/Krao/Grok"
