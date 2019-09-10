#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='pycvesearch',
    version='0.5',
    url='https://github.com/cve-search/PyCVESearch',
    author='Raphaël Vinot',
    author_email='raphael.vinot@circl.lu',
    license='Apache v2.0 License',
    packages=['pycvesearch'],
    description='A python wrapper around cve.circl.lu',
    long_description=open('README.md', 'rb').read().decode('UTF-8'),
    keywords=['CVE', 'API', 'wrapper'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Internet',
    ],
    tests_requires=['nose'],
    test_suite='nose.collector',
    install_requires=['requests'],
)
