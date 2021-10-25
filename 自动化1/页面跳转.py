from selenium import webdriver
import  time

driver = webdriver.Chrome()

driver.get(r"C:\Users\Administrator\Desktop\python自动化测试\自动化项目\自动化测试18\练习的html\跳转页面\pop.html")
driver.maximize_window()
driver.find_element_by_id("goo").click()
time.sleep(2)

driver.quit()