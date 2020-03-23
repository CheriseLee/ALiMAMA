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
        po = LoginPage(self.driver)
        f = open(current_path + "\\login_info.yml", 'r')
        datas = yaml.load(f)
        for key in datas['userlist']:
            po.login_action(key['username'], key['password'])
        sleep(3)
        f.close()
        # assert (self.driver.find_element_by_class_name("m-xs").is_displayed() == True)
        print("test_login1_normal is test end!")