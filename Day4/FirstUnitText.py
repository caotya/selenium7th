# 第一个单元测试框架代码
#1.引用unittest
import unittest
#2.创建类，编写自动化测试用例
class FirstUnitText(unittest.TestCase):
    #setup和tearDoen方法在每次执行时，每个方法都会执行一遍
    def setUp(self):
        print(1)
    def tearDown(self):
        print(2)
    def test_login(self):
        print(3)
    def switch_window(self):
        print(4)
    def test_zhuce(self):
        self.switch_window()
    #也可以选择重写setUpClass和taerDownClass方法
    @classmethod
    def setUpClass(cls):
         print(5)

    @classmethod
    def tearDownClass(cls):
        print(6)

if __name__ == '__main__':
   unittest.main()