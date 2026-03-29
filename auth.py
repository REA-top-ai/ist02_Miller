import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

user = 'kirill'
passwd = '1234'

url_basic = f'https://httpbin.org/basic-auth/{user}/{passwd}'
result = requests.get(url_basic, auth = HTTPBasicAuth(user, passwd))
print(result.json())

url_bearer = f'https://httpbin.org/bearer'
token = ('eyJhbGciOiJub25lIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImtpcmlsbCBtaWxsZXIiLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNzc0ODYzMjAwfQ.')
result2 = requests.get(url_bearer, headers = {'Authorization': f'Bearer {token}'})
print(result2.json())

url_diq = f'https://httpbin.org/digest-auth/auth/{user}/{passwd}'
print(requests.get(url_diq, auth=HTTPDigestAuth(user, passwd)).json())