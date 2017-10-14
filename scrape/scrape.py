from bs4 import BeautifulSoup
from selenium import webdriver
import re
import json

def scrape(json_file):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)

    raw_json = open(json_file, "r").read()
    config = json.loads(raw_json);

    browser.get(config["link"])
    soup = BeautifulSoup(browser.page_source,"html5lib")
    main = soup.main

    output = {}
    if "beds" in config:
        output["beds"] = config["beds"]
    else:
        pass
        #bed scrapping here

    if "bathrooms" in config:
        output["bathrooms"] = config["bathrooms"]
    else:
        pass
        #bed scrapping here

    #get all images
    images = []
    for img in main.find_all("img"):
        images.append(img["src"])
    output["images"] = images

    #find price
    price_pattern = re.compile("\$\d{3,4}")
    price_str = soup.find_all(text=price_pattern,recursive=True)

    price = int(re.search("\d+",price_str[0]).group())
    print price
    if config["rate"] == "per-person":
        output["price"] = price * output["beds"]
    else:
        output["price"] = price

    if config["info-given"]:
        output["info"] = config["info"]
    else:
        output["info"] = main.find_all(config["info"],recursive=True)

    print output

    # TODO: address, phone,beds,bathroom

if __name__ == "__main__":
    scrape("./json/309_2bed.json")
