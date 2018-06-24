import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Day5.myTestCase import MyTestCase


class login(MyTestCase):
    def test1(self):
        driver = self.driver
        driver.get("http://localhost/")
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/a[1]').click()
        driver.find_element_by_id("username").send_keys("cty")
        action = ActionChains(driver)
        # 所有的actions方法都要以perform()方法结尾才能被执行
        action.send_keys(Keys.TAB).send_keys("123456").perform()
        # 7.点击登陆按钮
        old_title = driver.title
        action.send_keys(Keys.ENTER).perform()
        time.sleep(10)
        login_text = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
        new_title = driver.title
        print(login_text)
        self.assertNotEqual(old_title,new_title)
        print(old_title)
        print(new_title)
        self.assertEqual(login_text,'您好 cty')
        # if old_title == new_title:
        #     print("测试失败")
        # else:
        #     print("测试成功")
if __name__ == '__main__':
    unittest.main()