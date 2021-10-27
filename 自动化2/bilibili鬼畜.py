from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome()

driver.get("http://www.bilibili.com")

driver.maximize_window()
time.sleep(5)

driver.find_element_by_xpath("//*[@id='nav_searchform']/input").send_keys("鬼畜")
driver.find_element_by_xpath("//*[@id='nav_searchform']/div").click()
time.sleep(5)
data = driver.window_handles   # ["s001","s002"]
driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='all-list']/div[1]/div[2]/ul/li[1]/a/div/div[3]").click()
