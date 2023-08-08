import time
from driver import Driver

driver = Driver()

if input("Start a saved game? (y/n): \n").lower() == "y":
    driver.import_save()

minutes = int(input("How many minutes do you want to run this game for?: \n"))
timeout = time.time() + 60 * minutes
time_check = time.time() + 1
time_check_2 = time.time() + 5

while True:
    if time.time() > timeout:
        break
    
    driver.cookie_btn.click()

    if time.time() > time_check:
        time_check += 1
        
        driver.check_upgrade()
        driver.check_hiring()

driver.export_save()

driver.quit()
