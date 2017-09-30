import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen('http://champaignmarshallapartments.com/110_E_John.html').read()

soup = BeautifulSoup(html, 'lxml')


lis = soup.find('ul', {'class', 'position2'}).find_all('li')

amenities = []

for li in lis:
    amenities.append(li.string)


for a in amenities:
    print a
