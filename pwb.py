# -*- coding: utf-8  -*-
u"""Foobar."""

import sys

#if PYPY:
#    print('', end='')

sys.path = (u'.', ) + tuple(sys.path[1:])

if __name__ == '__main__':
    print(__doc__)
