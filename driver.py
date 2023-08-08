import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

os.environ['PATH'] += r'/Users/jacobyoo/Desktop/PythonProjects/chromedriver'

class Driver(webdriver.Chrome):
    def __init__(self):
        super().__init__()
        self.get("https://orteil.dashnet.org/cookieclicker/")
        time.sleep(3)
        self.find_element(By.ID, "langSelect-EN").click()
        time.sleep(3)
        self.cookie_btn = self.find_element(By.ID, "bigCookie")
        self.upgrade = None
        self.bakers = []
        for i in range(20):
            self.bakers.append(self.find_element(By.ID, f"product{i}"))
        self.mute()
    
    def check_upgrade(self):
        try:
            self.upgrade = self.find_element(By.ID, "upgrade0")
            classes = self.upgrade.get_attribute("class").split()
            if "enabled" in classes:
                self.upgrade.click()
                self.upgrade = self.find_element(By.ID, "upgrade0")
        except NoSuchElementException:
            pass
        except Exception as e:
            print("Error:", e)
            raise Exception("An unexpected error occured")
    
    def check_hiring(self):
        for baker in self.bakers:
            classes = baker.get_attribute("class").split()
            if "enabled" in classes:
                baker.click()
                break
    
    def export_save(self):
        self.find_element(By.XPATH, '//*[@id="prefsButton"]/div').click()
        self.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[1]').click()
        with open("game_save.txt", "w") as file:
            file.write(self.find_element(By.ID, "textareaPrompt").text)
    
    def import_save(self):
        with open("game_save.txt", "r") as file:
            content = file.read()
            if content == "":
                print("Sorry but you have no saved game.")
            else:
                self.find_element(By.XPATH, '//*[@id="prefsButton"]/div').click()
                self.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[2]').click()
                self.find_element(By.ID, "textareaPrompt").send_keys(content + "\n")
                self.find_element(By.XPATH, '//*[@id="prefsButton"]/div').click()
        
    def mute(self):
        self.find_element(By.XPATH, '//*[@id="prefsButton"]/div').click()
        slider = self.find_element(By.ID, 'volumeSlider')
        ActionChains(self).click_and_hold(slider).move_by_offset(-200, 0).release().perform()
        time.sleep(5)
        self.find_element(By.XPATH, '//*[@id="prefsButton"]/div').click()
