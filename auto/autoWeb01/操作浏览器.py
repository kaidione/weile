# from selenium import webdriver
# import time
# # 创建谷歌浏览器对象
# chromeDriver = webdriver.Chrome()
#
# # 打开百度网址
# chromeDriver.get("http://www.baidu.com")
#
# # 窗口最大化
# chromeDriver.maximize_window()
#
# #寻找搜索输入框
# chromeDriver.find_element_by_id("kw").send_keys("java")
#
# # 点击百度一下按钮
# chromeDriver.find_element_by_id("su").click()
#
# time.sleep(3)
# # 退出浏览器
# chromeDriver.quit()
from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("https://www.douyu.com")

# 窗口最大化
# chromeDriver.maximize_window()
time.sleep(20)
#寻找搜索输入框
# chromeDriver.find_element_by_xpath("//*[@id='header-search-input']").click()
# chromeDriver.find_element_by_xpath("//*[@id='header-search-input']").click()
# chromeDriver.switch_to.active_element.send_key("王雨衫abc")
chromeDriver.find_element_by_xpath("//*[@id='header-search-input']").send_keys("王羽衫abc")
time.sleep(3)
# 点击百度一下按钮
chromeDriver.find_element_by_xpath("//*[@id='js-header']/div/div/div[3]/div[1]/div/div/span").click()
time.sleep(30)
chromeDriver.find_element_by_xpath("//*[@id='js-search-result']/section[3]/section[2]/section[1]/div[2]/ul/li/a").click()

# 退出浏览器
# chromeDriver.quit()