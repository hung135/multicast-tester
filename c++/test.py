import ctypes
#print ctypes.windll.cprog.square(4) # windows
x=ctypes.CDLL('/opt/lib/libctest.so') # linux

print(dir(x))
xxx=1
print(x.ctest2(xxx))