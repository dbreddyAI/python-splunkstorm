#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='splunkstorm',
    version='0.0.1',
    description='Log json to Splunkstorm.',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/python-splunkstorm',
    packages=['splunkstorm',],
    package_dir = {'splunkstorm': 'lib'},
    install_requires = ['requests==2.2.1'],
    license='MIT License',
    zip_safe=True)
