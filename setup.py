from setuptools import setup, find_packages
import os, sys

setup(name='dailymotion',
      version='0.0.1',
      description='Dailymotion API SDK',
      long_description='Dailymotion API SDK',
      download_url='https://github.com/dailymotion/dailymotion-sdk-python/archive/0.1.0.tar.gz',
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        ],
      keywords=['dailymotion', 'api', 'sdk', 'graph'],
      author='Samir AMZANI',
      author_email='samir.amzani@gmail.com',
      url='http://github.com/dailymotion/dailymotion-sdk-python',
      license='Apache License, Version 2.0',
      include_package_data=True,
      zip_safe=False,
      py_modules = ['dailymotion',],
      install_requires=[
          'requests',
          'pycurl'
      ],
)
