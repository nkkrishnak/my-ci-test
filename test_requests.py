import urllib3
import urllib3.contrib.pyopenssl

print('urllib3.connection.ssl_wrap_socket', urllib3.connection.ssl_wrap_socket)
print('urllib3.contrib.pyopenssl.ssl_wrap_socket', urllib3.contrib.pyopenssl.ssl_wrap_socket)

try:
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print(e)

print('urllib3.connection.ssl_wrap_socket', urllib3.connection.ssl_wrap_socket)
print('urllib3.contrib.pyopenssl.ssl_wrap_socket', urllib3.contrib.pyopenssl.ssl_wrap_socket)

print('id urllib3', id(urllib3))

import requests
import requests.packages
import requests.packages.urllib3
import requests.packages.urllib3.contrib.pyopenssl
import requests.packages.urllib3.connection
import requests.packages.urllib3.util

import OpenSSL

def print_module(module):
    filename = module.__file__
    if filename.endswith('c'):
        filename = filename[:-1]
    with open(filename, 'r') as f:
        print(f.read())

print('requests', requests.__version__)
try:
    print('requests pyopenssl', requests.pyopenssl, requests.pyopenssl.__file__)
except:
    print('requests pyopenssl doesnt exist')

print('orig_util_HAS_SNI', requests.pyopenssl.orig_util_HAS_SNI)
print('orig_connection_ssl_wrap_socket', requests.pyopenssl.orig_connection_ssl_wrap_socket)

print('requests __file__', requests.__file__)
print('requests urllib3 __file__', requests.packages.urllib3.__file__)
print('requests urllib3', requests.packages.urllib3.__version__)
print('id requests urllib3', id(requests.packages.urllib3))
print('urllib3', urllib3.__version__)
print('id urllib3', id(urllib3))

print('OpenSSL', OpenSSL.__version__)
print('OpenSSL __file__', OpenSSL.__file__)

from ndg.httpsclient.subj_alt_name import SubjectAltName
from pyasn1.codec.der import decoder as der_decoder
from ndg.httpsclient.ssl_peer_verification import SUBJ_ALT_NAME_SUPPORT
print('SUBJ_ALT_NAME_SUPPORT', SUBJ_ALT_NAME_SUPPORT)

#print('---- requests -----')
#print_module(requests)
#print('---------')

#print('---- requests.packages ----')
#print_module(requests.packages)
#print('--------')

print('requests urllib3 is urllib3', urllib3 is requests.packages.urllib3)
#print('requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket', requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

#print(requests.packages.urllib3, urllib3)

#print('uc,ruc,rup', urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

print('urllib3.util.HAS_SNI', urllib3.util.HAS_SNI)
try:
    print('urllib3.util.IS_PYOPENSSL', urllib3.util.IS_PYOPENSSL)
except:
    print('urllib3.util.IS_PYOPENSSL does not exist')

print('requests.packages.urllib3.util.HAS_SNI', requests.packages.urllib3.util.HAS_SNI)
try:
    print('requests.packages.urllib3.util.IS_PYOPENSSL', requests.packages.urllib3.util.IS_PYOPENSSL)
except:
    print('requests.packages.urllib3.util.IS_PYOPENSSL does not exist')

print('no inject 1:')
s = requests.Session()
s.get('https://www.wikipedia.org/')
s.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)

#print('no inject 2:')
#print('id urllib3', id(urllib3))

#s = requests.Session()
#s.get('https://www.wikipedia.org/')
#s.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)

#print('no inject 3:')

#s = requests.Session()
#s.get('https://www.wikipedia.org/')
#s.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)

try:
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print('EXCEPTION', e)

print('urllib3 inject:')

print('requests urllib3 is urllib3', urllib3 is requests.packages.urllib3)

print(requests.packages.urllib3, urllib3)
print('uc,ruc,rup', urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

print('requests.packages.urllib3.util.HAS_SNI', requests.packages.urllib3.util.HAS_SNI)
try:
    print('requests.packages.urllib3.util.IS_PYOPENSSL', requests.packages.urllib3.util.IS_PYOPENSSL)
except:
    print('util.IS_PYOPENSSL does not exist')

requests.get('https://www.wikipedia.org/')
requests.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)

try:
    requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print(e)

print('requests inject:')

print('requests urllib3 is urllib3', urllib3 is requests.packages.urllib3)

print(requests.packages.urllib3, urllib3)
print('uc,ruc,rup', urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.connection.ssl_wrap_socket, requests.packages.urllib3.contrib.pyopenssl.ssl_wrap_socket)

print('requests.packages.urllib3.util.HAS_SNI', requests.packages.urllib3.util.HAS_SNI)
try:
    print('requests.packages.urllib3.util.IS_PYOPENSSL', requests.packages.urllib3.util.IS_PYOPENSSL)
except:
    print('util.IS_PYOPENSSL does not exist')


requests.get('https://www.wikipedia.org/')
requests.get('https://testssl-expire-r2i2.disig.sk/index.en.html', verify=False)
