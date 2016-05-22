import ssl
import sys

import requests

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

s = requests.Session()
s.mount(url, Tls12HttpAdapter())
r = s.get(url)
print(r.status_code)
