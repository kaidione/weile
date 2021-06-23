from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://8.129.91.152:8765/")

driver.maximize_window()

driver.find_element_by_link_text("免费注册").click()

driver.find_element_by_xpath('//*[@id="phone"]').send_keys("17637923732")

time.sleep(10)

driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[3]/a').click()

time.sleep(1)

# data = driver.find_element_by_id("layui-layer5").find_element_by_class_name("layui-layer-content").text("验证码")
data = driver.find_element_by_class_name("layui-layer-content").text
# str = "验证码为4379"
# #
# a = str.split("验证码为")
# print(a)
a = data.split("验证码为")

driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[3]/input').send_keys(a[-1])

driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[4]/input').send_keys("123456qwe")

driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[5]/label').click()

driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div[6]/button').click()

time.sleep(1)

driver.find_element_by_link_text("系统自动分配").click()

time.sleep(5)
# print(data)
driver.quit()