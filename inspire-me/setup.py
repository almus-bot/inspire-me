from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import inspire-me

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='inspire-me',
    version=inspire-me.__version__,
    url='http://github.com/almus-bot/inspire-me/',
    license='BSD 3-Clause License',
    author='Francisco Palm',
    tests_require=['pytest'],
    install_requires=['Pillow>=3.0.0',
                    ],
    cmdclass={'test': PyTest},
    author_email='mapologo@tuta.io',
    description='Generator of inspirational images',
    long_description=long_description,
    packages=['inspire-me'],
    include_package_data=True,
    platforms='any',
    test_suite='inspire-me.test.test_inspire-me',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
