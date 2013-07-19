#!/bin/bash

VERSION_fastObjLoader=1.0
URL_fastObjLoader=http://localhost/download/fastObjLoader-$(echo $VERSION_fastObjLoader).tar.gz
DEPS_fastObjLoader=(python)
MD5_fastObjLoader=fa3d89b3df8d09bb6910ed082f6997db
BUILD_fastObjLoader=$BUILD_PATH/fastObjLoader/$(get_directory $URL_fastObjLoader)
RECIPE_fastObjLoader=$RECIPES_PATH/fastObjLoader

function prebuild_fastObjLoader() {
	true
}

function build_fastObjLoader() {
	cd $BUILD_fastObjLoader

	push_arm

	#dirty hack
	export C_INCLUDE="-I$ANDROIDNDK/sources/cxx-stl/gnu-libstdc++/$TOOLCHAIN_VERSION/include/ -I$ANDROIDNDK/sources/cxx-stl/gnu-libstdc++/$TOOLCHAIN_VERSION/libs/armeabi/include/"
	export OLD_BOUBOU=$CC
	export CC="$CXX $C_INCLUDE"

	try $BUILD_PATH/python-install/bin/python.host setup.py install -O2
	#try cp libgnustl_shared.so $LIBS_PATH/
	try cp $ANDROIDNDK/sources/cxx-stl/gnu-libstdc++/4.4.3/libs/armeabi/libgnustl_shared.so $LIBS_PATH/

	export CC=$OLD_BOUBOU
	pop_arm
}

function postbuild_fastObjLoader() {
	true
}
