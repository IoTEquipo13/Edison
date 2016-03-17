import requests


print "ANTES DEL GET"
response = requests.get('http://189.234.140.164:80')

print "despues del get"

assert response.status_code == 200

print response.json()
#open
