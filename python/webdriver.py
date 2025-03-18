#!/usr/local/bin/python3
# C:\InterSystems\Cache\bin>irispip install --upgrade --target C:\InterSystems\Cache\mgr\python selenium
# C:\InterSystems\Cache\bin>irispip install --target C:\InterSystems\Cache\mgr\python PyYaml

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
import base64
import time
import yaml

path = "C:\\InterSystems\\Cache\\mgr\\python\\chromedriver.exe"
service = Service(executable_path=path)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
#chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service, options=chrome_options)

def test():
    note = ''
    print("test")
    time.sleep(1)
    urlTest = "https://www.python.org/downloads/windows/"
    driver.get(urlTest)
    time.sleep(5)
    pdf_file = "C:\\InterSystems\\Cache\\CSP\\medkaz\\pdf\\test.pdf"
    pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
    pdf_data = base64.b64decode(pdf["data"])
    with open(pdf_file, "wb") as f:
        f.write(pdf_data)
    driver.quit()
    return note

test()
