from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='theme.deu',
      version=version,
      description="Skin para Direccion de Extensiones UNI",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='deu@uni.edu.ni',
      author_email='deu@uni.edu.ni',
      url='http://deu.googlecode.com/svn/trunk/theme.deu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['theme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
