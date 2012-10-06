#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

from blueprints.jars import __version__


setup(
    name='Blueprints.jars',
    version=__version__,
    url='https://github.com/tinkerpop/blueprints',
    license='BSD',
    author='Amirouche Boubekki',
    author_email='amirouche.boubekki@gmail.com',
    description='Java jars of Blueprints bundled as a Python package',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    platforms='POSIX',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
