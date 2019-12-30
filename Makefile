.PHONY: clean
#build the base docker image for building target environment
buildbase:
ifeq ("","$(docker images -q buildbase:latest 2> /dev/null)")
	docker build -t buildbase -f BuildBase.Dockerfile .
else
	echo "$(docker images -q buildbase:latest 2> /dev/null)"
endif
	

buildme: buildbase
	./buildme.sh

#compile local c library for testing
compile:
	cd scripts && python setup.py build_ext --inplace 

#clean out docker images
clean:
	docker rmi buildbase:latest
	docker image prune

