while 1:
  if(button.read() != 0):
	import requests
	url = 'https://greenheadapi.azurewebsites.net/user/test'
	data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
	response = requests.get(url, data=data)