from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
url = "https://www.instagram.com"

try:
    driver.get(url)
    time.sleep(1)
    email_input = driver.find_element(by.By.XPATH, "//*[@id=\"loginForm\"]/div/div[1]/div/label/input")
    password_input = driver.find_element(by.By.XPATH, "//*[@id=\"loginForm\"]/div/div[2]/div/label/input")
    email_input.send_keys("denirostik104@gmail.com")
    password_input.send_keys('46kD#@snlox')
    enter = driver.find_element(by.By.XPATH, "//*[@id=\"loginForm\"]/div/div[3]")
    enter.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.fullscreen_window()
    d = driver.find_element(by.By.TAG_NAME, "body")
    d.send_keys(Keys.ENTER)


    time.sleep(20)
except Exception as e:
    print(e)    

finally:
    driver.close()
    driver.quit()    