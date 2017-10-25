import scrape
import os
import json
from selenium import webdriver

def scrape_all(rel_directory):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), "chromedriver"), chrome_options=options)
    directory = os.path.join(os.getcwd(), rel_directory)
    #TODO go through all json files in directory
    apartments = {}
    for file in os.listdir(directory):
        if file.endswith(".json"):
            raw_json = open(os.path.join(directory,file),'r')
            config = json.load(raw_json)
            browser.get(config["link"])
            apartments[config["link"]] = scrape.scrape(browser.page_source,config)
    return apartments
