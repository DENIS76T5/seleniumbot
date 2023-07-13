
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
import time, pickle
from fake_useragent import UserAgent
user_agent = UserAgent().random

def click(x_path):
    button = driver.find_element(by.By.XPATH, x_path)
    button.click()

options = webdriver.FirefoxOptions()
options.add_argument("-profile")
options.add_argument("/Users/mac/library/Application Support/Firefox/profiles/du9nwate.default-release-1")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(options=options)
url = "https://www.instagram.com"
url2 ="https://opensea.io/"
url3 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url4 = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
try:
    driver.get(url4)
    driver.fullscreen_window()
    time.sleep(2)

    time.sleep(10)


# pickle.dump(driver.get_cookies(), open("cookie", "wb"))

except Exception as e:
    print(e)    

finally:
    driver.close()
    driver.quit()    