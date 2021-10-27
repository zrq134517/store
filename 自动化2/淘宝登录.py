from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 事件链对象
import  time
driver = webdriver.Chrome()

driver.get("http://www.taobao.com")

driver.maximize_window()

# 把driver交给ActionChians管理

driver.find_element_by_xpath("//*[@id='J_SiteNavLogin']/div[1]/div[1]/a[1]").click()


driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("13263515760")
driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("a13263515760")
time.sleep(3)


ac = ActionChains(driver)
ele = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]') # 滑块元素

time.sleep(2)
ac.click_and_hold(ele).move_by_offset(300,0).perform()# 立即执行
#点击 （）保持不动         移动*距离
ac.release() # 释放鼠标
