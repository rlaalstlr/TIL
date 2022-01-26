import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

response = requests.get(url)
doc = response.text

data = BeautifulSoup(doc, 'html.parser')

result = data.select_one('span.num.num2').text

print(result)