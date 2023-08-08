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

timeout = time.time() + 60 * 5

time_check = time.time() + 1

bakers = []
for i in range(20):
    bakers.append(driver.find_element(By.ID, f"product{i}"))

upgrade = None

while True:
    if time.time() > timeout:
        break
    cookie_btn.click()
    
    if time.time() > time_check:
        time_check += 1
        
        if upgrade == None:
            try:
                upgrade = driver.find_element(By.ID, "upgrade0")
            except:
                pass
        else:
            upgrade = driver.find_element(By.ID, "upgrade0")
            classes = upgrade.get_attribute("class").split()
            if "enabled" in classes:
                upgrade.click()
                upgrade = driver.find_element(By.ID, "upgrade0")
        
        for baker in bakers:
            classes = baker.get_attribute("class").split()
            if "enabled" in classes:
                baker.click()
        
        
                
            
    

driver.quit()
