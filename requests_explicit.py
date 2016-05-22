import ssl
import sys

import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class Tls12HttpAdapter(HTTPAdapter):
    """Transport adapter that allows forces use of TLSv1.2."""

    def init_poolmanager(self, connections, maxsize, block=False):
        """Pool manager constructor."""
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_version=ssl.PROTOCOL_TLSv1_2)


url = sys.argv[1]

s = requests.Session()
s.mount(url, Tls12HttpAdapter())
r = s.get(url)
print(r.status_code)
