import bs4
import requests

res = requests.get('https://www.amazon.in')
print(res.raise_for_status())
soup = bs4.BeautifulSoup(res.text, 'html.parser')

el = soup.select('a')
print(el)
print(len(el))
print(el[0].text)
print(el[0].get('href'))
print(el[0].get('title'))
print(el[0].attrs)

