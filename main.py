import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r'/Users/jacobyoo/Desktop/PythonProjects/chromedriver'
driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
driver.find_element(By.ID, "langSelect-EN").click()
time.sleep(3)

cookie_btn = driver.find_element(By.ID, "bigCookie")

t_end = time.time() + 60 * 5
while time.time() < t_end:
    cookie_btn.click()

driver.quit()
