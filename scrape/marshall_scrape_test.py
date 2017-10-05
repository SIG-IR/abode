import urllib2
import string_parser as sp
from bs4 import BeautifulSoup

def find_num_beds(string):
    if string.find('One bed') > -1 or string.find('1 bed') > -1:
        return 1
    elif string.find('Two bed') > -1 or string.find('2 bed') > -1:
            return 2
    elif string.find('Three bed') > -1 or string.find('3 bed') > -1:
            return 3
    else:
        return -1


#TODO REMOVE PRICE FROM INFO
def look_for_and_remove_price(info):
    prices = []
    price = {}
    for i in info:
        if find_num_beds(i) > -1 and i.find('$') > -1:
            price['num_beds'] = find_num_beds(i)
            price['monthly_rate'] = int(sp.find_price(i))
            prices.append(price)
            price = {}
        elif i.find('$') > -1:
            price['monthly_rate'] = int(sp.find_price(i))
        elif find_num_beds(i) > -1:
            price['num_beds'] = find_num_beds(i)

        if 'num_beds' in price and 'monthly_rate' in price:
            prices.append(price)
            price = {}

    return prices

def find_image_links(soup):
    img_links = []
    for img in soup.find_all('img'):
        img_links.append("http://champaignmarshallapartments.com/"  + img['src'])
    return img_links


def create_apartment_from_soup(soup, link):
    apartment_schema = {}
    apartment_schema['link'] = link
    apartment_schema['address'] = soup.find('h1', {'class', 'heading1'}).string
    apartment_schema['rate'] = look_for_and_remove_price(info)
    apartment_schema['pictures'] = find_image_links(soup)
    apartment_schema['landlord'] = {
            'email': None,
            'name': None,
            'phone': '217-356-1407'
    }

    print apartment_schema



apt_link = 'http://champaignmarshallapartments.com/105_E_John.html'

html = urllib2.urlopen(apt_link).read()

soup = BeautifulSoup(html, 'html5lib')

lis = soup.find('ul', {'class', 'position2'}).find_all('li')

info = []
visited_links = []

for li in lis:
    info.append(li.string)

for a in info:
    print a

find_image_links(soup)

create_apartment_from_soup(soup, apt_link)




'''
apartment schema: { link: String,
                    address: String,
                    rate: [LIST]{num_beds: Number,
                            monthly_rate: Number},
                    lat: String,
                    long: String,
                    landlord: { email: String,
                                name: String,
                                phone: String },
                    pictures: String[],
                    info: String[],
                    pets: Boolean
                }
'''
