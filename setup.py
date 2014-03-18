#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup


packages = [
    'boto3',
    'boto3.core',
    'boto3.sqs',
    'boto3.utils',
    'boto3.iam',
    'boto3.s3',
    'boto3.sns',
    'boto3.elastictranscoder'
]

requires = [
    'botocore==0.24.0',
    'six>=1.4.0',
    'jmespath==0.1.0',
    'python-dateutil>=2.1',
]

setup(
    name='boto3',
    version='unstable',
    description='Low-level, data-driven core of boto 3.',
    long_description=open('README.rst').read(),
    author='Amazon Web Services',
    author_email='garnaat@amazon.com',
    url='https://github.com/boto/boto3',
    scripts=[],
    packages=packages,
    package_data={
        'boto3': [
            'data/aws/resources/*.json',
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license=open("LICENSE").read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
