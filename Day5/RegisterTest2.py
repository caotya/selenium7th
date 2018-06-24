import unittest
import ddt
import time
from selenium import webdriver
# @ddt.ddt表示这个类实现了数据驱动测试
from selenium.webdriver.common.by import By

from Day5.csvFileMananger4 import CsvFileManager

# 2.
@ddt.ddt
class register2(unittest.TestCase):
    # 3.
    data_table = CsvFileManager().read('test_date.csv')
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
    #  4.为test_register方法添加装饰器@ddt.ddt，指定测试数据
    @ddt.data(*data_table)
    def test_register(self,row):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            # driver.find_element(By.Name,"username") == driver.find_element_by_name("username")
        driver.find_element(By.NAME,"username").send_keys(row[0])
        driver.find_element(By.NAME,"password").send_keys(row[1])
        driver.find_element(By.NAME,"userpassword2").send_keys(row[2])
        driver.find_element(By.NAME,"mobile_phone").send_keys(row[3])
        driver.find_element(By.NAME,"email").send_keys(row[4])
            # driver.find_element(By.CSS_SELECTOR,'[value="注册"]').click()
if __name__ == '__main__':
    unittest.main()