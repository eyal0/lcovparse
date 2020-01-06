#!/usr/bin/env python
from setuptools import setup

version = '0.0.4'
classifiers = ["Development Status :: 4 - Beta",
               "Environment :: Plugins",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: Apache Software License",
               "Topic :: Software Development :: Testing"]

setup(name='lcovparse',
      version=version,
      description="lcov to json",
      long_description=None,
      classifiers=classifiers,
      keywords='coverage',
      author='@codecov',
      author_email='hello@codecov.io',
      url='http://github.com/codecov/lcov-parse',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=['lcovparse'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      entry_points=None)
