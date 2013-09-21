#!/usr/bin/env python

from distutils.core import setup
import platform

def build_params():
    params = {
      'name':'copycat',
      'version':'0.0.6',
      'description':'easy way let use clip on command line with system clip',
      'author':'George Li',
      'author_email':'goblin.george@gmail.com',
      'url':'https://github.com/georgefs/copycat.git',
      'py_modules':['copycat'],
	  'license':'MIT',
      'install_requires': ['clime', ],
    }
    if platform.system() == 'Windows':
        params['scripts'] = ['copycat.bat']
    else:
        params['scripts'] = ['copycat']
    
    return params

setup(
    **build_params()
)

