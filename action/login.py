import os
import yaml
import drivers
from LoginPage import *
from time import *
from selenium.common.exceptions import NoSuchElementException

current_path = os.path.dirname(__file__)#使用不同py文件保证引文的文件路径固定


class Login():
    def login_normal(self):
        print('test login1_ normal is start run...')
        self.driver = drivers.browser()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        login = LoginPage(drivers)
        f = open(current_path + "\\login_info.yml", 'r')
        datas = yaml.load(f)
        for key in datas['userlist']:
            login.login_action(key['username'], key['password'])
        sleep(3)
        f.close()
        # assert (self.driver.find_element_by_class_name("m-xs").is_displayed() == True)
        print("test_login1_normal is test end!")

if __name__ == '__main__':
    Login().login_normal()
