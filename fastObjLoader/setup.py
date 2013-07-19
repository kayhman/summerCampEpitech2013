from distutils.core import setup
from distutils.extension import Extension

setup(name='fastObjLoader',
      version='1.0',
      ext_modules =  [Extension("fastObjLoader", ["fastObjLoader.cpp", "fastObjLoader_impl.cpp"], extra_link_args=[], extra_compile_args=[], 
	      libraries=['gnustl_shared'],
	      libraries_dir=['.']
)],
      data_files = [('.', ["fastObjLoader_impl.h"])],
            )
