.PHONY : clean
build:
	gcc -Wall -fPIC -c *.c
	gcc -shared -Wl,-soname,libctest.so.1 -o libctest.so.1.0   *.o
	mv libctest.so.1.0 /opt/lib
	ln -sf /opt/lib/libctest.so.1.0 /opt/lib/libctest.so.1
	ln -sf /opt/lib/libctest.so.1.0 /opt/lib/libctest.so
	ls -la /opt/lib/
clean:
	rm ctest1.o ctest2.o
	rm /opt/lib/libctest.so
	rm /opt/lib/libctest.so.1
	rm /opt/lib/libctest.so.1.0
	ls /opt/lib/ -la