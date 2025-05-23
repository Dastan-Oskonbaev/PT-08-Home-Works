import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/search/?term=")
# elements = driver.find_elements(By.CLASS_NAME, "movie-dummy")
# elements = driver.find_elements(By.TAG_NAME, "a")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(15)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(15)
# elements = driver.find_elements(By.XPATH, "//a[@class='movie-dummy']")
# button = driver.find_element(By.XPATH, "//a[@class='global_action_link']")
# button.click()
time.sleep(10)
# for element in elements:
#     source = element.get_attribute("href")
#     title = element.find_element(By.XPATH, ".//div[@class='movie-title']").text
#     image = element.find_element(By.XPATH, ".//img").get_attribute('src')

    # print(title)
    # print(image)
    # print(source)

driver.quit()

####

###

###

###
