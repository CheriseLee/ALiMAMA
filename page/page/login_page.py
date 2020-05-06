from selenium.webdriver.common.by import By
from base_page import BasePage
class LoginPage():
    #首页登录
    url = ''
    #封装定位器
    username_loc = (By.ID, 'fm-login-id')
    password_loc = (By.ID, 'fm-login-password')
    submit_loc = (By.CLASS_NAME, 'fm-button fm-submit password-login')

    '''页面基础类'''
    def __init__(self, driver):
        self.base_url = 'https://pub.alimama.com/'
        self.driver = driver
        self.timeout = 10 #设置超时等待

    def _open(self, url):
        url_ = self.base_url + url
        print("Test page is %s" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
    #
    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    #用户名输入框元素
    def type_username(self, driver,username):
        self
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #密码输入框元素
    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def login_action(self,driver, username, password):
        # self.open()
        # # 切换到登录的frame，解决找不到元素的问题
        # self.driver.switchTo("taobaoLoginIfr")
        # self.driver.switchTo("taobaoLoginIfr")
        self.type_username(driver,username)
        self.type_password(driver,password)
        self.type_submit(driver)

    # loginPass_loc = (By.LINK_TEXT, '我的空间')
    # loginFail_loc = (By.NAME, 'username')
    #
    # def type_login_pass_hint(self):
    #      return self.find_element(*self.loginPass_loc).text
    #
    # def type_login_fail_hint(self):
    #      return self.find_element(*self.loginFail_loc).text


