from ctypes import *
import os.path
path=os.path.dirname(__file__)
lib1 = cdll.LoadLibrary(path + '/lib/fann/libdoublefann.so')
lib2 = cdll.LoadLibrary(path + '/lib/libsvm.3.22/libsvm.so')
lib3 = cdll.LoadLibrary(path + '/lib/nomad/libnomad.so')
lib4 = cdll.LoadLibrary(path + '/lib/nomad/libsgtelib.so')
