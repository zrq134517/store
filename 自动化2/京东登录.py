from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.jd.com")

driver.maximize_window()

# 把driver交给ActionChians管理


driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("13263515760")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("a13263515760")

driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
