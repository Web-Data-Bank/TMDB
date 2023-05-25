from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("download_api.pyx")
)
