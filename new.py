import keyboard

TOKEN = "MTAxMjI5OTIxNzQyMDY4NTM1NA.GlC1DI.TGO2OExuWwm4XEZsMhi_pF9w43eMzFdcmCPgpc"

import win32
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
import cv2
cwd = os.getcwd()
os.environ['PATH'] += r"{}/chromedriver.exe".format(cwd)
driver = webdriver.Chrome()

driver.get('https://discord.com/channels/363985050578190336/838836195609280532')
driver.implicitly_wait(30)
# driver.fullscreen_window()

# a = driver.find_elements(By.CLASS_NAME, "contents-3ca1mk")
# a[1].click()
# width, height = pt.size()
# pt.moveTo(width/2, 0.625*height, duration=1)
# pt.click()
# time.sleep(5)
# driver.implicitly_wait(30)
pt.press("tab")
pt.press("tab")
pt.press("tab")
pt.press("tab")

pt.write("thmsbll85@gmail.com")
pt.press("tab")
pt.write("ZfjIejtb97s")
driver.implicitly_wait(12)
# c = driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
# c.click()
driver.implicitly_wait(30)

# # items = driver.find_elements(By.CLASS_NAME, "markup-eYLPri messageContent-2t3eCI")
# print(len(items))
# print(items)

# myname = driver.find_element(By.ID, "uid_10")
# mypass = driver.find_element(By.NAME, "password")
# #
# myname.send_keys("thmsbll85@gmail.com")
# myname.send_keys("ZfjIejtb97s")
time.sleep(12000)

