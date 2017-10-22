from bs4 import BeautifulSoup, Comment
from selenium import webdriver
import re
import json


def scrape(json_file):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(
        executable_path="./chromedriver", chrome_options=options)

    raw_json = open(json_file, "r").read()
    config = json.loads(raw_json)

    browser.get(config["link"])
    soup = BeautifulSoup(browser.page_source, "html5lib")

    #TODO: regex the content portion to work for all sites
    content = soup.find("div",id=["content"])
    if content == None:
        content = soup.find("div",class_=["page-content"])
    print content
    #remove all comments
    for comment in soup.body.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    output = {}

    # TODO: address
    address_regex = re.compile("^\d+\s[A-z]+\s[A-z]+", re.I)
    if "address" in config:
        output["address"] = config["address"]
    else:
        addresses = soup.find_all(recursive=True, text = address_regex)
        if len(addresses) == 1:
            output["address"] = re.search(address_regex, addresses[0]).group()
        for address in addresses:
            output["address"] = re.search(address_regex, address).group()
            if re.search("(location)", address, re.I) != None:
                break

    if "beds" in config:
        output["beds"] = config["beds"]
    else:
        #find full string
        beds_full_str = content.find(recursive=True, text=re.compile("\d (bed|br)",re.I))
        #find bed part
        if beds_full_str != None:
            print beds_full_str
            beds_str = re.search("\d (bed|br)", beds_full_str, re.I)
            if beds_str != None:
                beds = int(re.search("\d", beds_str.group()).group())
                output["beds"] = beds
        #find Number

        # bed scrapping here


    if "bathrooms" in config:
        output["bathrooms"] = config["bathrooms"]
    else:
        #find full string
        bathroom_full_str = content.find(recursive=True, text=re.compile("(\d (bath))",re.I))
        #find bathroom part
        #TODO handle if there are no bathrooms found
        if bathroom_full_str != None:
            bathroom_str = re.search("(\d (bath))", bathroom_full_str, re.I)
            if bathroom_str != None:
                bathroom = int(re.search("\d", bathroom_str.group()).group())
                output["bathrooms"] = bathroom

    # get all images
    #TODO: improve image scrapping
    images = []
    for img in content.find_all("img"):
        images.append(img["src"])
    #output["images"] = images

    # find price
    price_pattern = re.compile("\$\d{3,4}")
    price_str = content.find_all(text=price_pattern, recursive=True)
    price = int(re.search("\d+", price_str[0]).group())
    if config["rate"] == "per-person":
        output["price"] = price * output["beds"]
    else:
        output["price"] = price

    print output

if __name__ == "__main__":
    scrape("./json/test.json")
