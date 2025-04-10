import tkinter as tk
from tkinter import ttk
from db import db
from time import sleep
class AboutFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        # self.about_frame=tk.Frame(self.root)
        tk.Label(self,text="GUANYU").pack()
        tk.Label(self,text="SHEIA").pack()


class ChangeFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        # self.about_frame=tk.Frame(self.root)
        # tk.Label(self,text="修改页面").pack()
        self.name=tk.StringVar()
        self.math=tk.StringVar()
        self.chinese=tk.StringVar()
        self.english=tk.StringVar()
        self.status=tk.StringVar()
        # self.create_page()
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text="姓名:").grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)

        tk.Label(self, text="数学:").grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.math).grid(row=2, column=2, pady=10)

        tk.Label(self, text="语文:").grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.chinese).grid(row=3, column=2, pady=10)

        tk.Label(self, text="英语:").grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.english).grid(row=4, column=2, pady=10)

        tk.Button(self, text="查询", command=self.serach_by_name).grid(row=5, column=1, pady=10)

        tk.Button(self, text="修改",command=self.uodeta_stu ).grid(row=5, column=2, pady=1,stick=tk.E)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=5)
    def serach_by_name(self):
        flag,message =db.serach_name(self.name.get())
        self.status.set(message)
        # pass
    def uodeta_stu(self):
        print(self.name.get())
        flag,message=db.updata_by_stu(name=self.name.get(),math=self.math.get(),chinese=self.chinese.get(),english=self.english.get())
        self.status.set(message)

class InserFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        # self.about_frame=tk.Frame(self.root)
        # tk.Label(self,text="插入页面").pack()
        self.name=tk.StringVar()
        self.math=tk.StringVar()
        self.chinese=tk.StringVar()
        self.english=tk.StringVar()
        self.status=tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0,pady=10)

        tk.Label(self,text="姓名:").grid(row=1,column=1,pady=10)
        tk.Entry(self,textvariable=self.name).grid(row=1,column=2,pady=10)

        tk.Label(self,text="数学:").grid(row=2,column=1,pady=10)
        tk.Entry(self,textvariable=self.math).grid(row=2,column=2,pady=10)

        tk.Label(self,text="语文:").grid(row=3,column=1,pady=10)
        tk.Entry(self,textvariable=self.chinese).grid(row=3,column=2,pady=10)

        tk.Label(self,text="英语:").grid(row=4,column=1,pady=10)
        tk.Entry(self,textvariable=self.english).grid(row=4,column=2,pady=10)

        tk.Button(self,text="录入",command=self.recode_info).grid(row=5,column=2,pady=10)
        tk.Label(self,textvariable=self.status).grid(row=6,column=2,pady=5)

    def recode_info(self):
        stu={"name":self.name.get(),"math":self.math.get(),"chinese":self.chinese.get(),"english":self.english.get()}
        self.status.set("录入成功")
        db.insert(stu)
        # print(db.all())
        self.name.set('')
        self.math.set('')
        self.chinese.set('')
        self.english.set('')

class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # self.about_frame=tk.Frame(self.root)
        self.table_view=tk.Frame()
        self.table_view.pack()
        # tk.Label(self, text="查询页面").pack()
        self.create_page()

    def create_page(self):
        columns=("name","chinese","math","english")
        columns_values=("姓名","语文","数学","英语")
        self.tree_view=ttk.Treeview(self,show="headings",columns=columns)
        self.tree_view.column('name',width=88,anchor='center')
        self.tree_view.column('chinese',width=88,anchor='center')
        self.tree_view.column('math',width=88,anchor='center')
        self.tree_view.column('english',width=88,anchor='center')
        self.tree_view.heading('name',text="姓名")
        self.tree_view.heading('chinese',text="语文")
        self.tree_view.heading('math',text="数学")
        self.tree_view.heading('english',text="英语")
        self.tree_view.pack(fill=tk.BOTH,expand=True)
        self.show_data_frame()
        tk.Button(self,text="更新",command=self.show_data_frame).pack(anchor='e',pady=5)
    def show_data_frame(self):
        # print(db.all())
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass
        students =db.all()
        index=0
        for stus in students:
            # print(stus)
            self.tree_view.insert('',index=index+1,values=(
                stus['name'],stus['math'],stus['chinese'],stus['english'],
            ))
            # index+=1




class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # self.about_frame=tk.Frame(self.root)
        # tk.Label(self, text="删除页面").pack()
        self.name=tk.StringVar()
        self.statu=tk.StringVar()

        tk.Label(self,text="删除数据").grid(row=1,column=1,pady=10)
        tk.Label(self,text="根据名字删除信息").grid(row=2,column=1,)
        tk.Entry(self,textvariable=self.name).grid(row=3,column=1,)
        tk.Button(self,text='删除',command=self.delete).grid(row=3,column=2,)
        tk.Label(self,textvariable=self.statu).grid(row=4,column=1,padx=10 )

    def delete(self):
        username=self.name.get()
        flag,message=db.delete_by_name(username)
        self.statu.set(message)
