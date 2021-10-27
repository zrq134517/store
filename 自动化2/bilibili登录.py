from selenium import webdriver
import  time
driver = webdriver.Chrome()

driver.get("http://www.bilibili.com")

driver.maximize_window()
time.sleep(10)

driver.find_element_by_xpath("//*[@id='i_cecream']/div[1]/div[1]/ul[2]/li[1]/li/div[1]/div").click()

data = driver.window_handles   # ["s001","s002"]
driver.switch_to.window(data[1])
time.sleep(5)
driver.find_element_by_xpath("//*[@id='login-username']").send_keys("13263515760")
driver.find_element_by_xpath("//*[@id='login-passwd']").send_keys("a13263515760")


driver.find_element_by_xpath("//*[@id='geetest-wrap']/div/div[5]/a[1]").click()
