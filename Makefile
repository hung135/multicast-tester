.PHONY: clean
#build the base docker image for building target environment
buildbase:
	docker build -t buildbase -f BuildBase.Dockerfile .

buildme:
	./buildme.sh

#compile local c library for testing
compile:
	cd scripts && python setup.py build_ext --inplace 

#clean out docker images
clean:
	docker image prune