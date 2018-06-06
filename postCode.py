from requests import post, get
from settings import *


code = int(input())

response = post(ADRESS, data={'1': '2', 'code': code})

print(response)
print(response.text)