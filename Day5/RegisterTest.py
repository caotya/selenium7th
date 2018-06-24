import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Day5.csvFileMananger4 import CsvFileManager


class registerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()
    @classmethod
    def test_register(self):
        # driver.get("http://localhost")
        # zhuce_target = driver.find_element_by_link_text("注册")
        # driver.execute_script("arguments[0].removeAttribute('target')", zhuce_target)
        # zhuce_target.click()
        for row in CsvFileManager().read('test_date.csv'):
            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            # driver.find_element(By.Name,"username") == driver.find_element_by_name("username")
            driver.find_element(By.NAME,"username").send_keys(row[0])
            driver.find_element(By.NAME,"password").send_keys(row[1])
            driver.find_element(By.NAME,"userpassword2").send_keys(row[2])
            driver.find_element(By.NAME,"mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME,"email").send_keys(row[4])
            # driver.find_element(By.CSS_SELECTOR,'[value="注册"]').click()
            check_tip =  driver.find_element(By.CSS_SELECTOR,"form.registerform.sign> ul > li:nth-child(1) > div > span").text
            print(check_tip)
            self.assertEqual("用户名不低于三位，使用中文、数字、字母皆可！",check_tip)
if __name__ == '__main__':
    unittest.main()