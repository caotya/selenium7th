import unittest

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(self):
        time.sleep(30)
        self.driver.quit()
    def test_a_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()
        # 添加商品管理
    def test_b_product_manager(self):
        driver = self.driver
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #除了name切换mainFrame的方法，还可以通过8种元素定位，然后切换
        iframe = driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        driver.find_element_by_name("name").send_keys("饮水机")
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id('2').click()
        driver.find_element_by_id('6').click()
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        # select = driver.find_element_by_name("brand_id")
        # Select(select).select_by_visible_text("苹果 (Apple)")
        # driver.find_element_by_css_selector('[value="提交"]').click()
        select = Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_search").click()

if __name__ ==  '__main__':
    unittest.main()