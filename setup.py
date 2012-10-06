#!/usr/bin/env python
import os

from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


def long_description():
    path = os.path.dirname(__file__)
    path = os.path.join(path, 'README.rst')
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''


__doc__ = long_description()


class pytest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        # self.test_args = ['--pdb']
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)


from blueprints.jars import __version__


setup(
    name='Printemps',
    version=__version__,
    url='https://github.com/amirouche/Printemps',
    license='LGPL',
    author='Amirouche Boubekki',
    author_email='amirouche.boubekki@gmail.com',
    description='Python graph database lovestory',
    long_description=__doc__,
    packages=find_packages(exclude=["printemps/*.tests", "printemps/*.tests.*", "printemps/tests.*"]),
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
