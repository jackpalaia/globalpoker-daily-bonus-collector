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

from utils import get_browser, wait

load_dotenv()

browser = get_browser()
browser.get("https://www.globalpoker.com")

log_in = browser.find_element(
    By.XPATH, '//*[@id="gatsby-focus-wrapper"]/header/div[8]/a[2]')
log_in.click()
wait()

google_button = browser.find_elements(
    By.CLASS_NAME, "auth0-lock-social-button-text")[1]
google_button.click()
wait()

email_input = browser.find_element(
    By.ID, "Email")
email_input.click()
email_input.send_keys(os.getenv("GOOGLE_EMAIL"))

next_button_email = browser.find_element(By.ID, "next")
next_button_email.click()
wait()

password_input = browser.find_element(By.ID, "password")
password_input.click()
password_input.send_keys(os.getenv("GOOGLE_PASSWORD"))

next_button_password = browser.find_element(
    By.ID, "submit")
next_button_password.click()
wait()

cashier_button = browser.find_element(
    By.ID, "cashier-button")
cashier_button.click()
wait()

try:
    f = open(f"{os.getcwd()}/log.txt", "a")
    f.write(f"{datetime.now()}\n")

    first_clickable_bonus = browser.find_element(
        By.CSS_SELECTOR, "div[class='ffff_b ffff_o']")
    first_clickable_bonus.click()

    f.write(f"{first_clickable_bonus.get_attribute('title')} clicked\n")
    f.close()
except NoSuchElementException as e:
    f.write("no bonus available\n")
finally:
    f.write("\n")
    f.close()

browser.quit()
