from selenium import webdriver
from selenium.webdriver.common.by import By


class loginpage:
    # 在py中构造函数固定的名字__init__
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"
    username_input_loc = (By.NAME,"username")
    password_input_loc = (By.NAME,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")
    def open(self):
        self.driver.get(self.url)

    def input_username(self,username='cty'):
        # self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password='123456'):
        # self.driver.find_element(By.NAME,"password").send_keys(password)
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def cilck_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()