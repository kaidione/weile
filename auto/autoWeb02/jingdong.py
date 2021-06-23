from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.jd.com")

driver.maximize_window()

driver.find_element_by_link_text("你好，请登录").click()

# data = driver.window_handles
#
# driver.switch_to.window(data[1])

driver.find_element_by_link_text("账户登录").click()

driver.find_element_by_id("loginname").send_keys("13994754204")

driver.find_element_by_id("nloginpwd").send_keys("liwenhu1")

driver.find_element_by_id("loginsubmit").click()

time.sleep(5)

driver.find_element_by_link_text("手机").click()

data1 = driver.window_handles

driver.switch_to.window(data1[1])
time.sleep(5)
driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div/div/div[2]/div/div/div/div[2]/div/div[1]/img').click()

data2 = driver.window_handles

driver.switch_to.window(data2[2])

time.sleep(5)

driver.find_element_by_link_text("加入购物车").click()

driver.find_element_by_xpath('//*[@id="GotoShoppingCart"]').click()

time.sleep(5)

driver.quit()