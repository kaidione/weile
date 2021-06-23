from selenium import webdriver
import time

driver = webdriver.Chrome()

# driver.get(r"F:/Python自动化测试/自动化测试/自动化压缩包/自动化测试5/练习的html/练习的html/弹框的验证/dialogs.html")
driver.get(r"F:/Python自动化测试/自动化测试/自动化压缩包/练习的html/练习的html/跳转页面/pop.html")
driver.maximize_window()

# driver.find_element_by_id("confirm").click()
driver.find_element_by_id("goo").click()
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_id("kw").send_keys("java")

time.sleep(3)

# driver.switch_to.alert.dismiss()

driver.quit()

