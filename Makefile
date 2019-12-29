.PHONY: clean
buildbase:
	docker build -t buildbase -f BuildBase.Dockerfile .

buildme:
	buildme.sh

compile:
	python setup.py build_ext --inplace 

clean:
	docker image prune