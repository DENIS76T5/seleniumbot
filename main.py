
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time, pickle
from fake_useragent import UserAgent
user_agent = UserAgent().random

options = Options()
options.add_argument("-profile")
options.add_argument("/Users/mac/library/Application Support/firefox/profiles/z8jk1441.default-release-1")
options.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(options=options)
url = "https://www.instagram.com"
url2 ="https://opensea.io/"
url3 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
try:
    driver.get(url2)
    driver.fullscreen_window()
    time.sleep(2)


    driver.find_element(by.By.XPATH, "/html/body/div[1]/div/div[1]/div/nav/ul/div/div/div/div/div/button").click()
    time.sleep(1)
    driver.find_element(by.By.XPATH, "/html/body/div[5]/div/div/div/section/div/div[2]/div/ul/li[1]/button/div[2]").click()
    time.sleep(3)
    pidor = driver.find_element(by.By.XPATH, "//*[@id=\"password\"]")
    # pidor.send_keys("thWHL4HuM_vx-PF")
    # pickle.dump(driver.get_cookies(), open("cookie", "wb"))
    time.sleep(10)








#     time.sleep(202)
# except Exception as e:
#     print(e)    

finally:
    driver.close()
    driver.quit()    