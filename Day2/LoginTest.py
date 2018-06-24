#1.打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
class login():
    def loginWithDefaultUser(self,driver):
        #driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        #2.打开海盗商城网站
        driver.get("http://localhost/")
        #3.删除登陆链接的target属性
        #在python中字符串可以用单引号，也可以使用双引号
        #如果字符串本身包含双引号，两边使用单引号
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        #4.点击登陆按钮，跳转到登陆页面
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/a[1]').click()
        #5.输入用户名
        driver.find_element_by_id("username").send_keys("cty")
        #6.输入密码
        #ActionChains需要导包，导包快捷键alt+enter
        #action是动作行为的意思，chains是链表的意思，链表类似于数组
        #所以ActionChains是一组动作和行为的意思
        #下面这句话的意思是实例化一个ActionChains这个类的对象
        #这个对象可以用来执行一组动作和行为
        action=ActionChains(driver)
        #所有的actions方法都要以perform()方法结尾才能被执行
        action.send_keys(Keys.TAB).send_keys("123456").perform()
        #7.点击登陆按钮
        action.send_keys(Keys.ENTER).perform()
        #加入不支持回车键登陆，我们可以直接点击登陆按钮
        #加入也很难定位登陆系统，我还可以用submit()方法
        #submit是提交的意思,用于提交表单
        #想象一下，用户名和密码等信息是不是同时发送给后端服务端？
        #开发通过form表单把这些信息同时发送给后台