# -*- coding: utf-8  -*-
"""Installer script for Pywikibot 2.0 framework."""
from setuptools import setup, find_packages

name = 'pywikibot'
version = '3.0-dev'
github_url = 'https://github.com/wikimedia/pywikibot-core'

setup(
    name=name,
    version=version,
    description='Python MediaWiki Bot Framework',
    long_description=open('README.rst').read(),
    maintainer='The Pywikibot team',
    maintainer_email='pywikibot@lists.wikimedia.org',
    license='MIT License',
    packages=[str(name)] + [package
                            for package in find_packages()
                            if package.startswith('pywikibot.')],
    url='https://www.mediawiki.org/wiki/Pywikibot',
    test_suite="tests.collector",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    use_2to3=False
)
