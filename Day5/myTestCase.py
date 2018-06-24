# 封装setUpClass和tearDownClass方法
import unittest

import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()