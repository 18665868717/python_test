from tkinter import *
from tkinter.ttk import *
class Win_index:
    def __init__(self):
         self.root = self.__win()
         self.tk_label_frame_l749qkyu = Frame_l749qkyu(self.root)
         self.tk_label_l749r2t1 = self.__tk_label_l749r2t1()
         self.tk_button_chongxin_jiance = self.__tk_button_chongxin_jiance()
         self.tk_label_l749sy7u = self.__tk_label_l749sy7u()
         self.tk_label_l749u3gs = self.__tk_label_l749u3gs()
         self.tk_label_l749u9rv = self.__tk_label_l749u9rv()
         self.tk_label_l749udga = self.__tk_label_l749udga()
         self.tk_label_l749uj40 = self.__tk_label_l749uj40()
         self.tk_label_l749umdl = self.__tk_label_l749umdl()
         self.tk_label_l749uqyf = self.__tk_label_l749uqyf()
         self.tk_label_l749uudk = self.__tk_label_l749uudk()
         self.tk_label_l749v4sl = self.__tk_label_l749v4sl()
         self.tk_label_l749v9xb = self.__tk_label_l749v9xb()
         self.tk_label_l749vheb = self.__tk_label_l749vheb()
         self.tk_label_chuanganqi = self.__tk_label_chuanganqi()
         self.tk_button_chuanganqi = self.__tk_button_chuanganqi()
         self.tk_label_kaiguanji = self.__tk_label_kaiguanji()
         self.tk_label_fangchai = self.__tk_label_fangchai()
         self.tk_label_gps = self.__tk_label_gps()
         self.tk_label_4Gkaiji = self.__tk_label_4Gkaiji()
         self.tk_label_4Gbanben = self.__tk_label_4Gbanben()
         self.tk_label_4Gruwang = self.__tk_label_4Gruwang()
         self.tk_label_lanya = self.__tk_label_lanya()
         self.tk_label_chongdian = self.__tk_label_chongdian()
         self.tk_label_dianchi = self.__tk_label_dianchi()
         self.tk_label_4Gxinhao = self.__tk_label_4Gxinhao()
         self.tk_button_kaiguanji = self.__tk_button_kaiguanji()
         self.tk_button_fangchai = self.__tk_button_fangchai()
         self.tk_button_gps = self.__tk_button_gps()
         self.tk_button_4Gkaiji = self.__tk_button_4Gkaiji()
         self.tk_button_4Gbanben = self.__tk_button_4Gbanben()
         self.tk_button_4Gruwang = self.__tk_button_4Gruwang()
         self.tk_button_lanya = self.__tk_button_lanya()
         self.tk_button_chongdian = self.__tk_button_chongdian()
         self.tk_button_dianchi = self.__tk_button_dianchi()
         self.tk_button_4Gxinhao = self.__tk_button_4Gxinhao()
         self.tk_select_box_l74acz0x = self.__tk_select_box_l74acz0x()
         self.tk_button_saomiaochuankou = self.__tk_button_saomiaochuankou()
         self.tk_button_dakaichuankou = self.__tk_button_dakaichuankou()
         self.tk_button_baocunrizhi = self.__tk_button_baocunrizhi()
         self.tk_button_qingkongrizhi = self.__tk_button_qingkongrizhi()
    def __win(self):
         root = Tk()
         root.title("PCB功能检测")
         # 设置⼤⼩ 居中展⽰
         width = 1000
         height = 800
         screenwidth = root.winfo_screenwidth()
         screenheight = root.winfo_screenheight()
         geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
         root.geometry(geometry)
         root.resizable(width=False, height=False)
         return root
    def __tk_label_l749r2t1(self):
             label = Label(self.root,text="已打开")
             label.place(x=180, y=40, width=100, height=51)
             return label
    def __tk_button_chongxin_jiance(self):
         btn = Button(self.root, text="重新检测（全部）")
         btn.place(x=10, y=100, width=145, height=40)
         return btn
    def __tk_label_l749sy7u(self):
         label = Label(self.root,text="传感器")
         label.place(x=10, y=190, width=130, height=35)
         return label
    def __tk_label_l749u3gs(self):
         label = Label(self.root,text="电池功能")
         label.place(x=10, y=650, width=130, height=35)
         return label
    def __tk_label_l749u9rv(self):
         label = Label(self.root,text="开关机按按钮")
         label.place(x=10, y=250, width=130, height=35)
         return label
    def __tk_label_l749udga(self):
         label = Label(self.root,text="机械开关")
         label.place(x=10, y=300, width=130, height=35)
         return label
    def __tk_label_l749uj40(self):
         label = Label(self.root,text="gps功能")
         label.place(x=10, y=350, width=130, height=35)
         return label
    def __tk_label_l749umdl(self):
         label = Label(self.root,text="4G开机")
         label.place(x=10, y=400, width=130, height=35)
         return label
    def __tk_label_l749uqyf(self):
         label = Label(self.root,text="4G版本号")
         label.place(x=10, y=450, width=130, height=35)
         return label
    def __tk_label_l749uudk(self):
         label = Label(self.root,text="4G⼊⽹")
         label.place(x=10, y=500, width=130, height=35)
         return label
    def __tk_label_l749v4sl(self):
         label = Label(self.root,text="蓝⽛功能")
         label.place(x=10, y=550, width=130, height=35)
         return label
    def __tk_label_l749v9xb(self):
         label = Label(self.root,text="充电功能")
         label.place(x=10, y=600, width=130, height=35)
         return label
    def __tk_label_l749vheb(self):
         label = Label(self.root,text="4G信号")
         label.place(x=10, y=700, width=130, height=35)
         return label
    def __tk_label_chuanganqi(self):
         label = Label(self.root,text="传感器检测中")
         label.place(x=160, y=190, width=197, height=35)
         return label
    def __tk_button_chuanganqi(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=190, width=97, height=39)
         return btn
    def __tk_label_kaiguanji(self):
         label = Label(self.root,text="开关机按键检测中")
         label.place(x=160, y=250, width=197, height=35)
         return label
    def __tk_label_fangchai(self):
         label = Label(self.root,text="机械开关检测中")
         label.place(x=160, y=300, width=197, height=35)
         return label
    def __tk_label_gps(self):
         label = Label(self.root,text="GPS检测中")
         label.place(x=160, y=350, width=197, height=35)
         return label
    def __tk_label_4Gkaiji(self):
         label = Label(self.root,text="4G开机检测中")
         label.place(x=160, y=400, width=197, height=35)
         return label
    def __tk_label_4Gbanben(self):
         label = Label(self.root,text="4G版本检测中")
         label.place(x=160, y=450, width=197, height=35)
         return label
    def __tk_label_4Gruwang(self):
         label = Label(self.root,text="4G⼊⽹检测中")
         label.place(x=160, y=500, width=197, height=35)
         return label
    def __tk_label_lanya(self):
         label = Label(self.root,text="蓝⽛功能检测中")
         label.place(x=160, y=550, width=197, height=35)
         return label
    def __tk_label_chongdian(self):
         label = Label(self.root,text="充电功能检测中")
         label.place(x=160, y=600, width=197, height=35)
         return label
    def __tk_label_dianchi(self):
         label = Label(self.root,text="电池功能检测中")
         label.place(x=160, y=650, width=197, height=35)
         return label
    def __tk_label_4Gxinhao(self):
         label = Label(self.root,text="4G信号检测中")
         label.place(x=160, y=700, width=197, height=35)
         return label
    def __tk_button_kaiguanji(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=250, width=97, height=39)
         return btn
    def __tk_button_fangchai(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=300, width=97, height=39)
         return btn
    def __tk_button_gps(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=350, width=97, height=39)
         return btn
    def __tk_button_4Gkaiji(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=400, width=97, height=39)
         return btn
    def __tk_button_4Gbanben(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=450, width=97, height=39)
         return btn
    def __tk_button_4Gruwang(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=500, width=97, height=39)
         return btn
    def __tk_button_lanya(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=550, width=97, height=39)
         return btn
    def __tk_button_chongdian(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=600, width=97, height=39)
         return btn
    def __tk_button_dianchi(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=650, width=97, height=39)
         return btn
    def __tk_button_4Gxinhao(self):
         btn = Button(self.root, text="检测")
         btn.place(x=380, y=700, width=97, height=39)
         return btn
    def __tk_select_box_l74acz0x(self):
         cb = Combobox(self.root, state="readonly")
         cb['values'] = ("com", "com1", "com2")
         cb.place(x=10, y=20, width=146, height=55)
         return cb
    def __tk_button_saomiaochuankou(self):
         btn = Button(self.root, text="扫描串⼜")
         btn.place(x=310, y=20, width=115, height=47)
         return btn
    def __tk_button_dakaichuankou(self):
         btn = Button(self.root, text="打开串口")
         btn.place(x=310, y=90, width=115, height=47)
         # btn.bind("<Button-1>", out_txt())
         return btn
    def __tk_button_baocunrizhi(self):
         btn = Button(self.root, text="保存⽇志")
         btn.place(x=750, y=30, width=100, height=40)
         return btn
    def __tk_button_qingkongrizhi(self):
         btn = Button(self.root, text="清空⽇志")
         btn.place(x=600, y=30, width=100, height=40)
         return btn


class Frame_l749qkyu:
     def __init__(self,parent):
         self.root = self.__frame(parent)
     def __frame(self,parent):
        frame = LabelFrame(parent,text="标签容器")
        frame.place(x=490, y=80, width=467, height=686)
        return frame

def run():
     win = Win_index()
     def out_txt(event):
         win.tk_label_frame_l749qkyu


     win.tk_button_dakaichuankou.bind("<Button-1>",out_txt)




     # bt=win.tk_button_dakaichuankou
     # bt.bind("<Button-1>",out_txt)


     # bing=win.tk_button_saomiaochuankou
     # bing.bind("<Button>",out_txt())

     # TODO 绑定点击事件或其他逻辑处理
     win.root.mainloop()


if __name__ == "__main__":
    run()