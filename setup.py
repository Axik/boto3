#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import os
import sys
import boto3

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

packages = [
    'boto3',
]

requires = [
    'botocore==0.12.0',
    'six>=1.1.0',
    'jmespath==0.0.2',
    'python-dateutil>=2.1',
]

setup(
    name='boto3',
    version=boto3.__version__,
    description='Low-level, data-driven core of boto 3.',
    long_description=open('README.md').read(),
    author='Amazon Web Services',
    author_email='garnaat@amazon.com',
    url='https://github.com/boto/boto3',
    scripts=[],
    packages=packages,
    package_data={
        'boto3': [
            'data/*.json',
        ]
    },
    package_dir={
        'boto3': 'boto3'
    },
    include_package_data=True,
    install_requires=requires,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)
