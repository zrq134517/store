from selenium import webdriver
import  time
driver = webdriver.Chrome()

driver.get("http://www.qcc.com")

driver.maximize_window()
time.sleep(10)
driver.find_element_by_xpath("/html/body/header/div/ul/li[10]/a/span").click()
time.sleep(5)

driver.find_element_by_xpath("//*[@id='normalLogin']").click()
driver.find_element_by_xpath("//*[@id='nameNormal']").send_keys("13263515760")
driver.find_element_by_xpath("//*[@id='pwdNormal']").send_keys("a13263515760")
driver.find_element_by_xpath("//*[@id='user_login_normal']/button").click()

