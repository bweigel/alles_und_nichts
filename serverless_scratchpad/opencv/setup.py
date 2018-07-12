#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="Europace dNa",
    author_email='benjamin.weigel@europace.de',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    description="Template that contains a basic AWS lambda function alongside serverless and pytest for testing",
    install_requires=[],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='opencv-test',
    name='opencv-test',
    packages=find_packages(exclude=['*.test']),
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    url='https://github.com/hypoport/opencv-test',
    version='0.1.0',
    zip_safe=False,
)
