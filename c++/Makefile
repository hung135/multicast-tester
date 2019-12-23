build:
	gcc -Wall -fPIC -c *.c
	gcc -shared -Wl,-soname,libctest.so.1 -o libctest.so.1.0   *.o
	mv libctest.so.1.0 /opt/lib
	ln -sf /opt/lib/libctest.so.1.0 /opt/lib/libctest.so.1
	ln -sf /opt/lib/libctest.so.1.0 /opt/lib/libctest.so