
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
# options.add_argument("-headless")
options.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(options=options)

url = "https://www.instagram.com"
url2 = "https://opensea.io/"
url3 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url4 = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

try:
    driver.get(url4)
    driver.fullscreen_window()
    driver.implicitly_wait(2)
    click('/html/body/div[1]/div/div[1]/div/nav/ul/div/div/div/div/div/button/span')
    driver.implicitly_wait(4)
    click("/html/body/div[5]/div/div/div/section/div/div[2]/div/ul/li[1]/button/div[2]")
    # driver.switch_to.window(driver.window_handles[1])
    time.sleep(50)

except Exception as e:
    print(e)    

finally:
    driver.close()
    driver.quit()    



# for cookie in pickle.load(open ("cookie", "rb")):
    # driver.add_cookie(cookie)
# pickle.dump(driver.get_cookies(), open("cookie", "wb"))