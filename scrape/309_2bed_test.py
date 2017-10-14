from bs4 import BeautifulSoup
from selenium import webdriver
import re

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
    browser.get("https://www.americancampus.com/student-apartments/il/champaign/309-green/floor-plans/2-bedroom-1-bath")
    soup = BeautifulSoup(browser.page_source,"html5lib")
    main = soup.main
    for img in main.find_all("img"):
        print img["src"]
    price_pattern = re.compile("\$\d{3,4}")
    price = soup.find_all(text=price_pattern,recursive=True)
    print price
    info = main.find_all("li",recursive=True)
    print info
    # TODO: address, phone,

if __name__ == "__main__":
    main()
