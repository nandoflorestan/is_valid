#! /usr/bin/env python3
from setuptools import setup


setup(
    name='transvalid',
    py_modules=["transvalid"],
    license='MIT',
    version='0.9.0',
    description='Validation library that works in the browser via Transcrypt',
    author='Daan van der Kallen, Nando Florestan',
    author_email='nandoflorestan@gmail.com',
    url='https://github.com/nandoflorestan/transvalid',
    keywords=['validation', 'nested', 'predicates', 'transcrypt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    test_suite='tests',
    tests_require=['hypothesis>=3.21.2'],
)
