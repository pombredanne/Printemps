#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

from neo4j.jars import __version__


setup(
    name='Neo4j.jars',
    version=__version__,
    url='https://github.com/tinkerpop/blueprints',
    license='BSD',
    author='Amirouche Boubekki',
    author_email='amirouche.boubekki@gmail.com',
    description='Java jars of Neo4j bundled as a Python package',
    packages=find_packages(exclude=["neo4j.jars/*.tests", "neo4j.jars/*.tests.*", "neo4j.jars/tests.*"]),
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
