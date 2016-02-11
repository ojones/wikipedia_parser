from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
from os import path
import sys
import wikipedia_parser


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(name='wikipedia_parser',
      packages=find_packages(),
      version='0.1.2',
      description='Fetches wikipedia api resources and parses into data structures',
      author='Oswald Jones',
      author_email='wakeupoj@gmail.com',
      url='https://github.com/ojones/wikipedia_parser',
      download_url='https://github.com/ojones/wikipedia_parser/tarball/0.1',
      include_package_data=True,
      license='MIT',
      zip_safe=False,
      test_suite='wikipedia_parser.tests',
      tests_require=['pytest',
                     'tox',
                     ],
      cmdclass={'test': PyTest},
      install_requires=[
          'requests==2.3.0',
          'grequests==0.2.0',
          'mwclient>=0.7.2',
          'mwparserfromhell>=0.4.2',
          'wikipedia==1.4.0',
          'pytest==2.8.2',
          ],
      extras_require={
          'testing': ['pytest'],
      }
      )
