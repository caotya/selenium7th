from selenium import webdriver
# #1.登陆海盗商城登陆
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(20)
# driver.get("http://localhost/")
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/a[1]').click()
# driver.find_element_by_id("username").send_keys("cty")
# action=ActionChains(driver)
# action.send_keys(Keys.TAB).send_keys("123456").perform()
# action.send_keys(Keys.ENTER).perform()
# #2.点击个人账号
# driver.find_element_by_link_text("账号设置").click()
# #3.点击个人资料
# driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[4]/ul/li[2]/a").click()
# #4.修改真实姓名
# driver.find_element_by_id("true_name").send_keys("yyyy")
# #5.修改性别
# # 6.修改生日
# # 7.修改qq
# # 8.点击确定保存成功
from Day2.LoginTest import login
driver=webdriver.Chrome()
driver.implicitly_wait(20)
login().loginWithDefaultUser(driver)
driver.find_element_by_link_text("账号设置").click()