'''
    Browser/Server模式的软件：
        python
        pycharm
        selenium
        chromeDriver.exe
        浏览器技术选型：
            谷歌，火狐：
    client/server模式的软件：
'''
from selenium import webdriver
import  time
#  当前浏览器
driver = webdriver.Chrome()

# 打开页面
driver.get("http://www.baidu.com")

# 最大化
driver.maximize_window()

# 定位
driver.find_element_by_id("kw").send_keys("jason")

driver.find_element_by_id("su").click() # 点击

time.sleep(2)

driver.quit()





































