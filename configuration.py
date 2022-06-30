import requests

SERVICE_URL = 'https://shoponlain.herokuapp.com/prod-list/'
SERVICE_URL_DETAIL = 'https://shoponlain.herokuapp.com/prod-detail/1/'
SERVICE_URL_USER_API = 'https://gorest.co.in/public/v1/users'


resp = requests.get(SERVICE_URL_USER_API)
print(resp.headers)
