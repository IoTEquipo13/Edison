
import requests

files = {'file': open('plate4.jpg', 'rb')}


response = requests.post('http://189.234.140.164:8080/send-image', files=files)


assert response.status_code == 200

print response.json()
