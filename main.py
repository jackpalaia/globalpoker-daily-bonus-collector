import os
import os.path
import time
from datetime import datetime

from dotenv import load_dotenv
from pyotp import TOTP
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


# Setup chrome options
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
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

browser.get("https://www.globalpoker.com")

log_in = browser.find_element(
    By.XPATH, '//*[@id="gatsby-focus-wrapper"]/header/div[8]/a[2]')
log_in.click()

time.sleep(2)
google_button = browser.find_elements(
    By.CLASS_NAME, "auth0-lock-social-button-text")[1]
google_button.click()

time.sleep(2)
email_input = browser.find_element(
    By.ID, "Email")
email_input.click()
email_input.send_keys(os.getenv("GOOGLE_EMAIL"))

next_button_email = browser.find_element(By.ID, "next")
next_button_email.click()

time.sleep(2)
password_input = browser.find_element(By.ID, "password")
password_input.click()
password_input.send_keys(os.getenv("GOOGLE_PASSWORD"))

next_button_password = browser.find_element(
    By.ID, "submit")
next_button_password.click()

time.sleep(5)

cashier_button = browser.find_element(
    By.ID, "cashier-button")
cashier_button.click()

time.sleep(5)

f = open(f"{os.getcwd()}/log.txt", "a")
f.write(f"{datetime.now()}\n")

try:
    first_clickable_bonus = browser.find_element(
        By.CSS_SELECTOR, "div[class='ffff_b ffff_o']")
    first_clickable_bonus.click()

    f.write(f"{first_clickable_bonus.get_attribute('title')} clicked\n")
    f.close()
except NoSuchElementException as e:
    f.write("no bonus available\n")

f.write("\n")
f.close()

browser.quit()
