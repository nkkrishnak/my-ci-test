# -*- coding: utf-8  -*-
u"""Foobar."""

import sys

try:
    sys.pypy_version_info
    PYPY = True
except AttributeError:
    PYPY = False

#if PYPY:
#    print('', end='')

def set_sys_path():
    sys.path = (u'.', ) + tuple(sys.path[1:])

set_sys_path()

if __name__ == '__main__':
    if PYPY:
        print(__doc__)
