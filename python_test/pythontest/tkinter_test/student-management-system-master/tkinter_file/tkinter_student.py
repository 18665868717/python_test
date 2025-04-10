import tkinter as tk
from tkinter import messagebox
from db import db
from mianpage import MianPage as mainpage
class Login_page():
    def __init__(self,master):
        self.root=master
        self.root.geometry('300x150')
        self.root.title("学生管理系统")

        self.page_login=tk.Frame(root)
        self.page_login.pack()

        self.username=tk.StringVar()
        self.password=tk.StringVar()
        tk.Label(self.page_login,text="账户:").grid(row=1,column=1,pady=10)
        tk.Entry(self.page_login,textvariable=self.username).grid(row=1,column=2)
        tk.Label(self.page_login,text="密码:").grid(row=2,column=1,pady=10)
        tk.Entry(self.page_login,textvariable=self.password).grid(row=2,column=2)

        tk.Button(self.page_login,text="登录",command=self.login).grid(row=3,column=1)
        tk.Button(self.page_login,text="退出",command=self.page_login.quit).grid(row=3,column=2,sticky="e")
    def login(self):
        name=self.username.get()
        pwd=self.password.get()
        flag,message=db.check_login(name,pwd)
        if flag:
            self.page_login.destroy()
            mainpage(self.root)

        else:
            messagebox.showwarning(title="警告",message=message)

if __name__ == '__main__':
    root = tk.Tk()
    Login_page(master=root)
    root.mainloop()
