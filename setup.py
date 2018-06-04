#!/usr/bin/env python

from setuptools import setup, find_packages

pkgs = find_packages()

setup(
    name='typedclass',
    version='0.0.AUTOVERSION',
    description='typedclass',
    author='Ostrovok Company',
    author_email='hi@ostrovok.ru',
    ext_modules=[],
    packages=pkgs,
    scripts=[],
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
)
