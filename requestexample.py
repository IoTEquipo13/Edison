import requests
response = requests.get('https://greenheadapi.azurewebsites.net/api/user/getUser/Expreso')
assert response.status_code == 200
print response.json();	
"""
for repo in response.json():
    print '[{}] {}'.format(repo['language'], repo['name'])"""
