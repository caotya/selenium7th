# 1.登陆海盗商城后台
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver =  webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).send_keys("password").send_keys(Keys.ENTER).perform()

driver.find_element_by_name("userverify").send_keys("1234")
actions.send_keys(Keys.ENTER).perform()
# 2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
# 3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
# 4.输入商品名称
# driver.find_element_by_name("name").send_keys("iphone")
driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(1) > input")
# 5.选择商品分类（双击分类或者是选择当前分类）
# driver.find_element_by_id("1").click()
# 6.在下拉框中选择商品品牌
# 7.点击提交按钮