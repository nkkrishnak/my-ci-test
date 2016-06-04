import requests
import requests.packages.urllib3
import requests.packages.urllib3.contrib.pyopenssl

import urllib3
import urllib3.contrib.pyopenssl

print('requests', requests.__version__)
print('requests urllib3', requests.packages.urllib3.__version__)
print('urllib3', urllib3.__version__)

try:
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print(e)

try:
    requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()
except Exception as e:
    print(e)

requests.get('https://www.wikipedia.org/')
requests.get('https://testssl-expire-r2i2.disig.sk/index.en.html')
