# distutils: language = c++
# distutils: sources = fastObjLoader_impl.cpp

#import numpy as np
#cimport numpy as np
from libcpp.vector cimport vector

#cdef extern void cpp_calculate_normal(const float* vertices, const int* idx, int size)
#cdef extern int cpp_loadObjFile(const char* name, float*& vertices, int*& idx)
cdef extern from "fastObjLoader_impl.h":
	cdef int cpp_loadObjFile(const char* name, vector[float]& vertices, vector[int]& idx)

def loadObjFile(const char* filename):
	cdef vector[float] vertices
	cdef vector[int] triangles

	cpp_loadObjFile(filename, vertices, triangles)

	return vertices, triangles

	
#def calculate_normal(np.ndarray[float, ndim=1, mode="c"] vs, np.ndarray[int, ndim=1, mode="c"] idx, int size):
#	calculate_normal_impl(<float*>vs.data, <int*>idx.data, size)
