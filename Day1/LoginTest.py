import time
from selenium import webdriver

driver = webdriver.Chrome()
#设置隐形等待，一旦找到页面元素，马上执行后面的语句，如果超过20s，仍然找不到页面元素，那么程序将超时报错
driver.implicitly_wait(20)
driver.get("http://localhost/")
#dr=driver.find_element_by_class_name("header")
#dr.find_elements_by_tag_name("index.php?m=user&c=public&a=login")
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("cty")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()

#6.检查是否成功
#因为不能马上加载出被检测的控jian，所以需要加入时间等待
#time.sleep(5)
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)

#if语句判断显示的文本和预期的文本是否一致
if username_text == '您好 cty':
    print("测试执行成功")
else:
    print("测试执行失败")

#7.点击进入商城购物
#driver.find_element_by_xpath().click()
#driver.find_element_by_link_text("进入商城购物").click()
#8.商城主页搜索iphone手机
driver.find_element_by_name("keyword").send_keys("iphone")
#9.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#10.在搜索结果页面，点击第一个商品的图片
driver.find_element_by_class_name("shop_01").click()
driver.close()
#11.点击加入购物车
#页面跳转：0表示第一个窗口,1表示第二个,当你用driver.close()关闭一个之后, 第二个窗口就变成了第一个,所以推荐用-1
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id("joinCarButton").click()
