from setuptools import setup, find_packages
import os

version = '0.1a1'

install_requires = [
    'cromlech.browser',
    'cromlech.io',
    'grokcore.component',
    'setuptools',
    'zope.component',
    'zope.interface',
    'zope.location',
    ]

tests_require = [
    'cromlech.browser [test]',
    'grokcore.component',
    'pytest',
    'zope.testing',
    ]

setup(name='dolmen.location',
      version=version,
      description="URL computing using locatability (``zope.location``)",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Dolmen Location',
      author='The Dolmen team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://gitweb.dolmen-project.org/',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['dolmen',],
      include_package_data=True,
      zip_safe=False,
      tests_require = tests_require,
      install_requires = install_requires,
      extras_require = {'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
