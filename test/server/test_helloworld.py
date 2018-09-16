import requests

#url = 'https://agrino-sigfox-backend.heroku.com:80/'
url = 'http://localhost:1984'
r = requests.get(url)
print(r.status_code)
