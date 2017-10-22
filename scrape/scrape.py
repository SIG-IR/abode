from bs4 import BeautifulSoup
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
    body = soup.body

    output = {}

    # TODO: address

    if "beds" in config:
        output["beds"] = config["beds"]
    else:
        #find full string
        beds_full_str = soup.find(recursive=True, text=re.compile("\d (bed)",re.I))
        #find bed part
        #TODO handle if no beds found
        beds_str = re.search("\d (bed)", beds_full_str, re.I).group(0)
        #find Number
        beds = int(re.search("\d", beds_str).group(0))
        output["beds"] = beds
        # bed scrapping here


    if "bathrooms" in config:
        output["bathrooms"] = config["bathrooms"]
    else:
        #find full string
        bathroom_full_str = soup.find(recursive=True, text=re.compile("(\d (bath))",re.I))
        #find bathroom part
        #TODO handle if there are no bathrooms found
        bathroom_str = re.search("(\d (bath))", bathroom_full_str, re.I).group(0)
        #find Number
        bathroom = int(re.search("\d", bathroom_str).group(0))
        output["bathrooms"] = bathroom
        # bed scrapping here

    # get all images
    #TODO: improve image scrapping
    images = []
    for img in body.find_all("img"):
        images.append(img["src"])
    output["images"] = images

    # find price
    price_pattern = re.compile("\$\d{3,4}")
    price_str = soup.find_all(text=price_pattern, recursive=True)
    print price_str
    price = int(re.search("\d+", price_str[0]).group())
    print price
    if config["rate"] == "per-person":
        output["price"] = price * output["beds"]
    else:
        output["price"] = price

    print output

if __name__ == "__main__":
    scrape("./json/309_2bed.json")
