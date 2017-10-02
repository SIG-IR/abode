import urllib2
from bs4 import BeautifulSoup

def find_num_beds(string):
    if string.find('One bed') > -1:
        return 1
    elif string.find('Two bed') > -1:
            return 2
    elif string.find('Three bed') > -1:
            return 3
    elif string.find('Four bed') > -1:
        return 4
    else:
        return -1

def find_price(string):
    index_of_dollar = string.find('$')
    index_of_next_space = string.find(' ', index_of_dollar)
    if index_of_dollar > -1 and index_of_next_space > -1:
        return string[index_of_dollar + 1: index_of_next_space]
    else:
        return -1

def look_for_and_remove_price(amenities):
    prices = []
    price = {}
    for a in amenities:
        if find_num_beds(a) > -1 and a.find('$') > -1:
            price['num_beds'] = find_num_beds(a)
            price['monthly_rate'] = int(find_price(a))
            prices.append(price)
            price = {}
        elif a.find('$') > -1:
            price['monthly_rate'] = int(find_price(a))
        elif find_num_beds(a) > -1:
            price['num_beds'] = find_num_beds(a)

        if 'num_beds' in price and 'monthly_rate' in price:
            prices.append(price)
            price = {}

    return prices


def create_apartment_from_soup(soup, link):
    apartment_schema = {}
    apartment_schema['link'] = link
    apartment_schema['address'] = soup.find('h1', {'class', 'heading1'}).string
    apartment_schema['rate'] = look_for_and_remove_price(amenities)

    print apartment_schema




html = urllib2.urlopen('http://champaignmarshallapartments.com/105_E_John.html').read()

soup = BeautifulSoup(html, 'lxml')

lis = soup.find('ul', {'class', 'position2'}).find_all('li')

amenities = []
visited_links = []

for li in lis:
    amenities.append(li.string)

#for link in soup.findAll('a', href=True):
    #print "http://champaignmarshallapartments.com/" + link['href']

for a in amenities:
    print a

create_apartment_from_soup(soup, 'http://champaignmarshallapartments.com/110_E_John.html')




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
                    amenities: String[]
                }
'''
