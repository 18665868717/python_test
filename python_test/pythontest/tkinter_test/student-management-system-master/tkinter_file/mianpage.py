import tkinter as tk
from views import AboutFrame
from views import ChangeFrame,SearchFrame,DeleteFrame,InserFrame
class MianPage:
    def __init__(self,master:tk.Tk):
        self.root=master
        self.root.geometry('600x400')
        self.root.title("管理系统")
        self.create_page()

    def create_page(self):
        self.about_frame=AboutFrame(self.root)
        self.change_frame=ChangeFrame(self.root)
        self.searchframe=SearchFrame(self.root)
        self.dele=DeleteFrame(self.root)
        self.inser=InserFrame(self.root)

        menuber=tk.Menu(self.root)
        menuber.add_command(label="录入",command=self.show_inser)
        menuber.add_command(label="查询",command=self.show_search)
        menuber.add_command(label="删除",command=self.show_del)
        menuber.add_command(label="修改",command=self.shou_change)
        menuber.add_command(label="关于",command=self.show_about)
        self.root['menu']=menuber
    def show_inser(self):
        self.about_frame.pack_forget()
        self.change_frame.pack_forget() #遗忘页面
        self.searchframe.pack_forget()
        self.dele.pack_forget()
        self.inser.pack()
    def show_del(self):
        self.about_frame.pack_forget()
        self.change_frame.pack_forget() #遗忘页面
        self.searchframe.pack_forget()
        self.dele.pack()
        self.inser.pack_forget()
    def show_search(self):
        self.about_frame.pack_forget()
        self.change_frame.pack_forget() #遗忘页面
        self.searchframe.pack()#显示页面
        self.dele.pack_forget()
        self.inser.pack_forget()
    def show_about(self):
        self.about_frame.pack()
        self.change_frame.pack_forget() #遗忘页面
        self.searchframe.pack_forget()
        self.dele.pack_forget()
        self.inser.pack_forget()
    def shou_change(self):
        self.about_frame.pack_forget()
        self.change_frame.pack() #遗忘页面
        self.searchframe.pack_forget()
        self.dele.pack_forget()
        self.inser.pack_forget()


if __name__ == '__main__':
    root=tk.Tk()
    MianPage(master=root)
    root.mainloop()