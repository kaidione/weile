from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")

ac = ActionChains(driver)

driver.find_element_by_link_text("电脑办公").click()

time.sleep(5)

data = driver.window_handles

time.sleep(5)

driver.switch_to.window(data[1])

driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div[2]/ul/li[2]').click()

time.sleep(5)

data1 = driver.window_handles

time.sleep(5)

driver.switch_to.window(data1[2])

time.sleep(5)

driver.find_element_by_link_text("加入购物车").click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[39]/div/div[2]/div/div[1]/a').click()

time.sleep(10)

driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.suning.com")
# # driver.maximize_window()
#
# driver.find_element_by_link_text("手机").click()
# # driver.find_element_by_xpath()
#
# time.sleep(19)
# # driver.quit()

