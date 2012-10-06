#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages


from orientdb.jars import __version__


setup(
    name='OrientDB.jars',
    version=__version__,
    url='https://code.google.com/p/orient/',
    license='Apache',
    author='Amirouche Boubekki',
    author_email='amirouche.boubekki@gmail.com',
    description='Java jars of OrientDB bundled as a Python package',
    packages=find_packages(exclude=["orientdb.jars/*.tests", "orientdb.jars/*.tests.*", "orientdb.jars/tests.*"]),
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
