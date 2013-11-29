#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='dpaste',
    version='2.0',
    description='dpaste is a Django based pastebin. It\'s intended to run '
                'separately but its also possible to be installed into an '
                'existing Django project like a regular app.',
    long_description=open('README.rst').read(),
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='https://github.com/bartTC/dpaste/',

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ),

    packages=find_packages(),
    package_data={'dpaste': ['static/*.*', 'templates/*.*']},
    scripts=('manage.py',),
    install_requires=(
        'django>=1.4',
        'django-mptt>=0.6.0',
        'pygments>=1.6',
        'requests>=2.0.0',
    ),
)
