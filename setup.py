from setuptools import setup, find_packages
import os

version = '0.1b1'

install_requires = [
    'cromlech.browser >= 0.3a2',
    'cromlech.io >= 0.2a1',
    'grokcore.component',
    'setuptools',
    'zope.component',
    'zope.interface',
    'zope.location',
    ]

tests_require = [
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
