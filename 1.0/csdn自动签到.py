from selenium import webdriver
import time
from tkinter import messagebox
import sys
user=input("请输入用户名")
password=input("请输入密码")
driver=webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://passport.csdn.net/login?code=public")
driver.find_element_by_link_text("账号密码登录").click()
driver.find_element_by_css_selector("[placeholder='手机号/邮箱/用户名']").send_keys(user)
driver.find_element_by_css_selector("[placeholder='密码']").send_keys(password)
driver.find_element_by_css_selector("button").click()
new_window='window.open("{}")'.format("https://i.csdn.net/#/uc/profile")#js函数，此方法适用于所有的浏览器
driver.execute_script(new_window)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "个人" in driver.title:
        break
new_window = 'window.open("{}")'.format("https://i.csdn.net/#/uc/reward")  # js函数，此方法适用于所有的浏览器
driver.execute_script(new_window)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "签到" in driver.title:
        break


if(driver.find_element_by_xpath("//div[@class='handle_box has_sign']")):
    messagebox.showinfo("错误", "您已经签到过了")
    driver.quit()
    sys.exit(1)

try:
    elem=driver.find_element_by_xpath("//div[@class='handle_box to_sign']")
except:
    messagebox.showinfo("错误", "没有找到对应的元素")
    driver.quit()
    sys.exit(1)
else:
    elem.click()

driver.quit()