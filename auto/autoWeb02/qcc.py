from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.qcc.com")

driver.maximize_window()

ac = ActionChains(driver)

driver.find_element_by_link_text("登录 | 注册").click()

time.sleep(6)

ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

ac.click_and_hold(ele).move_by_offset(384, 0).perform()

time.sleep(3)

driver.quit()
