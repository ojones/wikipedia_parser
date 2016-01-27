from setuptools import setup

__author__ = 'oswaldjones'


setup(name='wikipedia_parser',
      version='0.1.0',
      description='Fetches wikipedia api resources and parses into data structures',
      author='Oswald Jones',
      author_email='wakeupoj@gmail.com',
      packages=['wikipedia_parser'],
      zip_safe=False,
      test_suite='nose.collector',
      setup_requires=['nose>=1.0'],
      install_requires=[
          'requests==2.3.0',
          'grequests==0.2.0',
          'mwclient==0.7.2',
          'mwparserfromhell==0.4.2',
          'wikipedia==1.4.0',
          'pytest==2.8.2'],
      )
