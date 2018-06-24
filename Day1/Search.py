from selenium import webdriver
driver = webdriver.Chrome()
#1.打开主页面
driver.get("http://localhost/")
#2.进入登陆页面
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/a[1]").click()
#3.输入iphone
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_name("keyword").send_keys("iphone")
#以上的案例中，步骤2到3会发生页面跳转，如果我们想在新的的标签页上操作页面元素，需要进行窗口切换
#需要用到driver.switch_to.window(driver.window_handles[1])
#driver.window_handles可以理解为一个数组，[1]表示数组的第二个元素
#所以，第二个窗口的名字就是driver.window_handles[1]
#[1]表示第二个元素，[-1]表示最后一个元素
#在python中元组和列表可以正着从0开始数，也开始负着从-1开始数，倒数第一个-1，倒数第二个-2
#所以上面的窗口名称也可以改为：driver.window_handles[-1]

