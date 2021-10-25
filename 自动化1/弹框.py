'''
    任务1：
        把练习的html除了滑动验证，其他做一下
    任务2：
        京东的搜索商品、详情，添加购物车
        淘宝的登陆自行研究
        苏宁，搜索一个商品，添加购物车
'''


from selenium import webdriver
import  time

driver = webdriver.Chrome()

driver.get(r"C:\Users\Administrator\Desktop\python自动化测试\自动化项目\自动化测试18\练习的html\弹框的验证/dialogs.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='confirm']").click()

driver.switch_to.alert.accept()  #accept()  确定
driver.switch_to.alert.dismiss() # 取消
time.sleep(2)

driver.quit()



