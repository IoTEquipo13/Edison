import requests


print "ANTES DEL GET"
response = requests.get('https://104.44.133.248/plate')

print "despues del get"

assert response.status_code == 200

print response.json()
#open
