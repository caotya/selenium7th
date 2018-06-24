import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
driver.get("http://localhost/")
Login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",Login_link)
Login_link.click()
# 输入账号密码登陆
driver.find_element_by_id("username").send_keys("cty")
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
# 返回商城首页
driver.find_element_by_partial_link_text("返回商城首页").click()
# 搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
# 点击商品（用这种方法再实现一遍）
# document.getElementsByClassName("shop_01-imgbox")[0].childNodes[1].removeAttribute('target')
# document.getElementsByClassName("shop_01 fl")[0].childNodes[1].removeAttribute("target")
Image_Link=driver.find_element_by_css_selector("div.protect_con > div > div.shop_01-imgbox > a")
driver.execute_script("arguments[0].removeAttribute('target')",Image_Link)
Image_Link.click()
#加入购物车
driver.find_element_by_id("joinCarButton").click()
#去购物车结算
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算
driver.find_element_by_css_selector(".shopCar_btn_03").click()
#点击添加新地址
driver.find_element_by_css_selector(".add-address").click()
#输入收货人等信息

#省
dropdown = driver.find_element_by_id("add-new-area-select")
# print(type(dropdown))
time.sleep(5)
select1 = Select(dropdown)
select1.select_by_visible_text("辽宁省")
# Select(dropdown).select_by_visible_text("辽宁省")

# 市
DropdownCity = driver.find_elements_by_class_name("add-new-area-select")[1]
# select2 = Select(DropdownCity)
# select2.select_by_visible_text("吉林市")
Select(DropdownCity).select_by_visible_text("沈阳市")

# 区
DropdownArea = driver.find_elements_by_class_name("add-new-area-select")[2]
Select(DropdownArea).select_by_visible_text("和平区")

# dropdown_area = driver.find_elements_by_tag_name("select")[2]
