import datetime
import os
import time
import requests
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pt

if __name__ == '__main__':
    now = datetime.datetime.now()

    cwd = os.getcwd()
    os.environ['PATH'] += r"{}/chromedriver.exe".format(cwd)
    driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()

    browser = uc.Chrome(
        options=options,
    )
    try:
        browser.get("https://www.immowelt.de/")
        browser.implicitly_wait(30)
        # btn = driver.find_element(By.CLASS_NAME, "/html/body/div[2]//div/div/div[2]/div/div[2]/div/div/div/div[2]/button[2]")
        # print(btn)
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]//div/div/div[2]/div/div[2]/div/div/div/div[2]/button[2]")))
        okbtn = browser.find_element(By.XPATH,
                                    "/html/body/div[2]//div/div/div[2]/div/div[2]/div/div/div/div[2]/button[2]")
        okbtn.click()
        HomeMultipleChoice = browser.find_element(By.ID, "spanSearchWhat")
        ZipcodeInput = browser.find_element(By.ID, "tbLocationInput")
        seekBTN = browser.find_element(By.ID, "btnSearchSubmit")
        time.sleep(12000)

    except:
        print("didn't work")
        browser.quit()









