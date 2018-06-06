from requests import get, post
from settings import *

response = get(ADRESS)

print(response)
print(response.text)