try:
    import setuptools  # noqa
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup

classifiers = ['Development Status :: 4 - Beta'
              , 'Environment :: Console'
              , 'Intended Audience :: Developers'
              , 'License :: OSI Approved :: MIT License'
              , 'Natural Language :: English'
              , 'Operating System :: MacOS :: MacOS X'
              , 'Operating System :: Microsoft :: Windows'
              , 'Operating System :: POSIX'
              , 'Programming Language :: Python :: 2.6'
              , 'Programming Language :: Python :: 2.7'
              , 'Programming Language :: Python :: Implementation :: CPython'
              , 'Programming Language :: Python :: Implementation :: Jython'
              , 'Topic :: Internet :: WWW/HTTP :: HTTP Servers'
               ]

setup( author = 'Chad Whitacre'
     , author_email = 'chad@zetaweb.com'
     , classifiers = classifiers
     , description = ('jinja2 plugin for Aspen')
     , name = 'aspen-jinja2'
     , entry_points = { 'aspen.renderers' : 'jinja2=aspen_jinja2_renderer',
                      }
     , py_modules = [ 'ez_setup', 'aspen_jinja2_renderer' ]
     , url = 'http://aspen.io/'
     , version = '0.4'
     , zip_safe = False
     , install_requires = ['aspen>=0.23',
                           'jinja2>=2.7.0']
      )
