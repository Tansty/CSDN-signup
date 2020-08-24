from selenium import webdriver
from tkinter import messagebox
import sys
import tkinter
from tkinter import *

class gui(object):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("CSDN自动签到")  #标题
        self.init_window_name.geometry()   #设置窗口大小，设置窗口位置
        self.init_label=Label(self.init_window_name,text="账号： ")
        self.init_label.grid()#x=0,y=0
        self.user=Entry(self.init_window_name)   #创建输入框
        self.user.grid(row=0,column=1)
        self.init_label2=Label(self.init_window_name,text="密码： ")
        self.init_label2.grid(row=1,column=0)
        self.password=Entry(self.init_window_name)
        self.password.grid(row=1,column=1)
        self.w=Button(text="签到", bg="lightblue", width=10,command=self.driver)
        self.w.grid()

    def driver(self):
        user=self.user.get()
        password=self.password.get()
        if not user or not password:
            messagebox.showerror("警告","请输入账号和密码")
            return
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

        try:
            elem=driver.find_element_by_xpath("//div[@class='handle_box has_sign']")
        except:
            print("您有可能还未签到或可以抽奖")
        else:
            messagebox.showinfo("错误", "您已经签到过了")
            driver.quit()
            sys.exit(1)
        #如果已经完成签到就退出

        try:
            elem=driver.find_element_by_xpath("//div[@class='handle_box to_reward']")
        except:
            print("您还未签到")
        else:
            messagebox.showinfo("恭喜", "您可以去抽奖了")
            driver.quit()
            sys.exit(1)

        #提示可以抽奖
        try:
            elem=driver.find_element_by_xpath("//div[@class='handle_box to_sign']")
        except:
            messagebox.showinfo("错误", "没有找到对应的元素")
            driver.quit()
            sys.exit(1)
        else:
            elem.click()
        #签到
        driver.quit()

def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    sign = gui(init_window)
    # 设置根窗口默认属性
    sign.set_init_window()
    init_window.mainloop()  # 父窗口进入事件循环，可以
    #理解为保持窗口运行，否则界面不展示

gui_start()