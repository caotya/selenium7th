# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# from Day5.myTestCase import MyTestCase
#
#
# class loginest2(MyTestCase):
#     def test1(self):
#         driver = self.driver
#         driver.get("http://localhost/")
#         driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
#         driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/a[1]').click()
#         driver.find_element_by_id("username").send_keys("cty")
#         action = ActionChains(driver)
#         # 所有的actions方法都要以perform()方法结尾才能被执行
#         action.send_keys(Keys.TAB).send_keys("123456").perform()
#         # 7.点击登陆按钮
#         action.send_keys(Keys.ENTER).perform()
#         time.sleep(10)
#         # 通过判断导航栏中是否存在用户名，登陆是否成功
#         welcomeText = driver.find_element(By.PARTIAL_LINK_TEXT,"你好").text
#         self.assertEqual(welcomeText,"您好 cty")

#  ------------------------------------------------------------------------------->>>>>>
# 调用loginpage类中封装好的open()
# 实例化Loginpage的对象
from Day5.myTestCase import MyTestCase
from Day5.page_object.LoginPage import loginpage
class LoginTest2(MyTestCase):
    def test_login(self):
        login_page = loginpage(self.driver)
        login_page.open()
        login_page.input_username()
        login_page.input_password()
        login_page.cilck_login_button()
