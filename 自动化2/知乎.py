from selenium import webdriver
import  time
driver = webdriver.Chrome()

driver.get("http://www.zhihu.com")

driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]").click()

driver.find_element_by_name("username").send_keys("13263515760")
driver.find_element_by_name("password").send_keys("a13263515760")
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[1]/div/div[1]/form/button").click()
