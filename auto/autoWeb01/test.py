from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get(r"F:/Python自动化测试/自动化测试/自动化压缩包/练习的html/练习的html/上传文件和下拉列表/autotest.html")

driver.maximize_window()

driver.find_element_by_id("accountID").send_keys("小朋友")
driver.find_element_by_id("passwordID").send_keys("123456")
driver.find_element_by_xpath("//*[@value = 'beijing']").click()
driver.find_element_by_xpath("//*[@id = 'sexID2']").click()
driver.find_element_by_xpath("//*[@name = 'u3' and @value = 'spring']").click()
driver.find_element_by_xpath("//*[@name = 'u3' and @value = 'winter']").click()
driver.find_element_by_xpath("//*[@name = 'file' and @type = 'file']").send_keys(r"E:\studyfile\P图\变绘画.jpg")
driver.find_element_by_id("buttonID").click()
time.sleep(3)
driver.switch_to.alert.dismiss()

time.sleep(5)

driver.close()
