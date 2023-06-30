import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def wait():
    time.sleep(3)


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument('--disable-dev-shm-usage')

    webdriver_service = Service("/usr/bin/chromedriver")
    browser = webdriver.Chrome(
        service=webdriver_service, options=chrome_options)

    return browser
