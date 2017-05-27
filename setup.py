# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="data-structures",
    description='This module will hold examples of classic data structures implemented using Python.',
    version='0.1',
    author='Munir Ibrahim',
    author_email='mibrah04@gmail.com',
    package_dir={'': 'src'},
    install_requires=['pytest', 'pytest-cov', 'ipython'],
    extras_require={
        'test': ['tox']
    }
)