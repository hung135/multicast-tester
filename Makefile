.PHONY: clean
buildme:
	./buildme.sh

compile:
	python setup.py build_ext --inplace 