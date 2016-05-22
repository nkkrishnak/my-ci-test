import ssl
import sys

import requests

from requests.utils import urlparse
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class Tls12HttpAdapter(HTTPAdapter):
    """Transport adapter that forces use of TLSv1.2."""

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_version=ssl.PROTOCOL_TLSv1_2)


url = sys.argv[1]

if len(sys.argv) > 2:
    mounted_url = sys.argv[2]
else:
    parsed_url = urlparse(url)
    mounted_url = '{0}://{1}'.format(parsed_url.scheme, parsed_url.hostname)

print('mounting TLSv1.2 adapter on {0}'.format(mounted_url))

s = requests.Session()
s.mount(mounted_url, Tls12HttpAdapter())
r = s.get(url)
print(r.status_code)
