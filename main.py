import requests

r = requests.post('https://httpbin.org/delay/6', timeout=3)

print(r)