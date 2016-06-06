'''
Debian and other distributions "unbundle" requests' vendored dependencies, and
rewrite all imports to use the global versions of ``urllib3`` and ``chardet``.
The problem with this is that not only requests itself imports those
dependencies, but third-party code outside of the distros' control too.

In reaction to these problems, the distro maintainers replaced
``requests.packages`` with a magical "stub module" that imports the correct
modules. The implementations were varying in quality and all had severe
problems. For example, a symlink (or hardlink) that links the correct modules
into place introduces problems regarding object identity, since you now have
two modules in `sys.modules` with the same API, but different identities::

    requests.packages.urllib3 is not urllib3

With version ``2.5.2``, requests started to maintain its own stub, so that
distro-specific breakage would be reduced to a minimum, even though the whole
issue is not requests' fault in the first place. See
https://github.com/kennethreitz/requests/pull/2375 for the corresponding pull
request.
'''

from __future__ import absolute_import
import sys

try:
    from . import urllib3
except ImportError:
    import urllib3
    import urllib3.util
    #import urllib3.connection
    print('(inside requests.packages.__init__) id urllib3.util', id(urllib3.util))
    print('(inside requests.packages.__init__) urllib3.util.HAS_SNI', urllib3.util.HAS_SNI)
    print('(inside requests.packages.__init__) urllib3.util.IS_PYOPENSSL', urllib3.util.IS_PYOPENSSL)

    sys.modules['%s.urllib3' % __name__] = urllib3
    sys.modules['%s.urllib3.util' % __name__] = urllib3.util
    sys.modules['%s.urllib3.connection' % __name__] = urllib3.connection

    import requests.packages.urllib3.util
    
    print('(inside requests.packages.__init__) id requests.packages.urllib3.util', id(urllib3.util))
    print('(inside requests.packages.__init__) urllib3.requests.packages.util.HAS_SNI', urllib3.util.HAS_SNI)
    print('(inside requests.packages.__init__) urllib3.requests.packages.util.IS_PYOPENSSL', urllib3.util.IS_PYOPENSSL)

try:
    from . import chardet
except ImportError:
    import chardet
    sys.modules['%s.chardet' % __name__] = chardet
