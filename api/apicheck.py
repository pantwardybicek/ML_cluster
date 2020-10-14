import requests

r = requests.get('http://localhost:8000/')
print (r.content)

r = requests.post('http://localhost:8000/svc')
print (r.content)

r = requests.post('http://localhost:8000/fgh', params = {"hfff":"1311"})
print (r.content)

r = requests.post('http://localhost:8000/fgh')
print (r.content)