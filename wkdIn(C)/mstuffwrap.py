from ctypes import cdll
lib = cdll.LoadLibrary('./stuff.so')

n1 = 'Hi'
n2 = 'Bye'

lib.func(n1,n2)
