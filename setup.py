from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules= cythonize('receiver.pyx'))

# python setup.py build_ext --inplace 