# Thir-party (pip install)

import requests
response = requests.get('https://petstore.swagger.io/v2/store/inventory')
print(response.json())  # Automatically handles JSON