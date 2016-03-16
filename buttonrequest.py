import requests
import mraa

button = mraa.Gpio(2)
button.dir(mraa.DIR_IN)

while 1:
	placa = 'ashjo'
	if(button.read() != 0):
		response = requests.get('https://greenheadapi.azurewebsites.net/api/place/getzone/' + placa)
		#assert response.status_code == 200
		#print response.status_code
		if(response.status_code == 500):
			continue
		else:
			#print response.raw.read(10)
			#print response.content
			print response.json();
		"""
		for repo in response.json():
			print '[{}]
		{};.format(repo['language'],
		repo['name'])"""

