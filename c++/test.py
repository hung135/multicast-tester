import ctypes
#print ctypes.windll.cprog.square(4) # windows
x=ctypes.CDLL('/opt/lib/libctest.so') # linux

print(dir(x))
xxx=1
xx_int=ctypes.c_int()
print(x.ctest2(xxx))

print(x.ctest1(ctypes.byref(xx_int)))