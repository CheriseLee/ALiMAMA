import os
import yaml
import drivers
from login_page import *
from time import *
from page import *
from selenium.common.exceptions import NoSuchElementException

current_path = os.path.dirname(__file__)#使用不同py文件保证引文的文件路径固定


class LoginAction():
    def login_normal(self):

        self.driver = drivers.browser() #获取浏览器驱动
        self.driver.implicitly_wait(5)#等5s
        self.driver.maximize_window() #窗口最大化
        # self.driver.get("https://pub.alimama.com/") #打开对应的页面
        po = LoginPage(self.driver)
        f = open(current_path + "\\login_info.yml", 'r')
        datas = yaml.load(f) #从本地文件获取用户名密码
        po.open()
        # # 切换到登录的frame，解决找不到元素的问题
        self.driver.switchTo("taobaoLoginIfr")
        po.login_action(datas['username'], datas['password'])
        sleep(3)
        f.close()
        # assert (self.driver.find_element_by_class_name("m-xs").is_displayed() == True)
        print("test_login1_normal is test end!")

if __name__ == '__main__':
    LoginAction().login_normal()
