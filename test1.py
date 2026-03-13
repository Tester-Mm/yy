import sys
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 打开浏览器
browser = webdriver.Chrome()
# 最大化打开窗口
browser.maximize_window()
browser.get("https://plat.dev.winxuan.com")
# 出现证书问题导致无法直接跳转，模拟点击高级-继续访问
browser.find_element(By.ID, "details-button").click()
browser.find_element(By.ID, "proceed-link").click()
time.sleep(3)
# 查找登录的用户名
browser.find_element(By.XPATH, "/html/body/div/div[2]/div/nz-modal-container/div/div/div/form/div[""2]/nz-form-item[""1]/nz-form-control/div/div/nz-input-group/input").send_keys("yuyue2")
# 查找登录的密码
browser.find_element(By.XPATH, "/html/body/div/div[2]/div/nz-modal-container/div/div/div/form/div[""2]/nz-form-item[""2]/nz-form-control/div/div/nz-input-group/input").send_keys("YUYUE1024")
# 点击登录按钮
browser.find_element(By.XPATH, "/html/body/div/div[2]/div/nz-modal-container/div/div/div/form/div[2]/nz-form-item[""3]/nz-form-control/div/div/button").click()
time.sleep(3)
