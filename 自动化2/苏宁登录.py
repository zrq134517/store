from selenium import webdriver
import  time
driver = webdriver.Chrome()

driver.get("http://www.suning.com")

driver.maximize_window()

# 把driver交给ActionChians管理

driver.find_element_by_xpath("//*[@id='reg-bar-node']/a[1]").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a[2]").click()

driver.find_element_by_xpath("//*[@id='userName']").send_keys("13263515760")
driver.find_element_by_xpath("//*[@id='password']").send_keys("a13263515760")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='iar1_sncaptcha_button']").click()