#!/usr/bin/env python
# -*- coding: utf-8  -*-
"""Wrapper script to use Pywikibot in 'directory' mode.

Run scripts using:

    python pwb.py <name_of_script> <options>

and it will use the package directory to store all user files, will fix up
search paths so the package does not need to be installed, etc.
"""
# (C) Pywikibot team, 2016
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, print_function, unicode_literals
__version__ = '$Id: 88e40ee4eaea1c630b4dc7d61fa3639afae8fc22 $'

# The following snippet was developed by Ned Batchelder (and others)
# for coverage [1], with python 3 support [2] added later,
# and is available under the BSD license (see [3])
# [1] https://bitbucket.org/ned/coveragepy/src/b5abcee50dbe/coverage/execfile.py
# [2] https://bitbucket.org/ned/coveragepy/src/fd5363090034/coverage/execfile.py
# [3] https://bitbucket.org/ned/coveragepy/src/2c5fb3a8b81c/setup.py?at=default#cl-31

import sys
import os

#if PYPY:
#    print('', end='')

sys.path = [sys.path[0], '.',
            os.path.join('.', 'pywikibot', 'compat'),
            ] + sys.path[1:]


def main():
    pass

if __name__ == '__main__':
    if not main():
        print(__doc__)
