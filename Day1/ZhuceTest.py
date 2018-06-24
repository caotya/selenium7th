from selenium import webdriver
import time
driver= webdriver.Chrome()
driver.get("http://localhost/")
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("1112")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("15235923261")
driver.find_element_by_name("email").send_keys("123256@qq.com")
driver.find_element_by_class_name("reg_btn").click()
time.sleep(5)
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)