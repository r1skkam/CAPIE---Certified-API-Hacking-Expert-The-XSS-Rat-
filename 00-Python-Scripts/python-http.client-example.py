# Built-in (Standard Library)

import http.client
conn = http.client.HTTPSConnection("petstore.swagger.io")
conn.request("GET", "/v2/store/inventory")
response = conn.getresponse()
print(response.read().decode())  # Manual decoding required
