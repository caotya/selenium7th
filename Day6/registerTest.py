import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Day5.myTestCase import MyTestCase
from Day6.DBconnection import DBconnection


class RigisterTest(MyTestCase):
    def test_register(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys("jinx212")
        driver.find_element(By.NAME, "password").send_keys("123562")
        driver.find_element(By.NAME, "userpassword2").send_keys("123562")
        driver.find_element(By.NAME, "mobile_phone").send_keys("15256893145")
        driver.find_element(By.NAME, "email").send_keys("4545854@qq.com")
        driver.find_element(By.CSS_SELECTOR, '[value="注册"]').click()
        time.sleep(2)
        new_record = DBconnection().ececute_sql_command(sql)
        self.assertEqual("jinx212",new_record[1])
        print(new_record)