from distutils.core import setup
from Cython.Build import cythonize

setup(name='fastObjLoader',
      version='1.0',
      ext_modules = cythonize("fastObjLoader.pyx")
      )
