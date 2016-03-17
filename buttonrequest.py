import requests
import mraa

button = mraa.Gpio(2)
button.dir(mraa.DIR_IN)

while 1:
	placa = 'Expreso'
	if(button.read() != 0):
		response = requests.get('https://greenheadapi.azurewebsites.net/api/user/getUser/' + placa)
		assert response.status_code == 200
		print response.json();
		"""
		for repo in response.json():
			print '[{}]
		{};.format(repo['language'],
		repo['name'])"""

