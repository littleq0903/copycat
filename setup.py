#!/usr/bin/env python

from distutils.core import setup
import platform

def build_params():
    params = {
      'name':'copycat',
      'version':'0.0.1',
      'description':'easy way let use clip on command line with system clip',
      'author':'George Li',
      'author_email':'goblin.george@gmail.com',
      'url':'https://github.com/georgefs/copycat.git',
      'py_modules':['CopyCat'],
	  'license':'MIT',
      'scripts': ['copycat'],
      'install_requires': ['clime', ],
    }
    
    return params

setup(
    **build_params()
)

