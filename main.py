import os
import time

from selenium.webdriver.common.by import By

from utils import get_browser

while True:
    browser = get_browser()

    browser.get("https://www.globalpoker.com")

    login_button = browser.find_element(
        By.XPATH, '//*[@id="gatsby-focus-wrapper"]/header/div[8]/a[2]')
    login_button.click()
    time.sleep(10)

    email = browser.find_element(By.XPATH, '//*[@id="1-email"]')
    email.click()
    email.send_keys(os.getenv("EMAIL"))

    password = browser.find_element(
        By.XPATH, '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/input')
    password.click()
    password.send_keys(os.getenv("PASSWORD"))

    login = browser.find_element(
        By.XPATH, '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button')
    login.click()
    time.sleep(10)

    shop = browser.find_element(By.XPATH, '//*[@id="cashier-button"]/span[2]')
    shop.click()
    time.sleep(10)

    for i in range(1, 8):
        bonus = browser.find_element(By.XPATH, f'//*[@id="daily-bonus-{i}"]')
        bonus.click()
        time.sleep(5)

    browser.quit()

    with open("log.txt", "a+") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")

    time.sleep(21600)
