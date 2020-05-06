#coding=utf-8

from selenium import webdriver
import time

browser=webdriver.Firefox()

browser.get("https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
sreach_window=browser.current_window_handle  #此行代码用来定位当前页面

browser.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[3]/div[4]/h3/a").click()
time.sleep(5)
