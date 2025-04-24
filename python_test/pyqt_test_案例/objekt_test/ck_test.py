import sys
import serial
import threading
class Uart(object):
     def __init__(self,port,baud):
        self.err=0
        self.uart_statu = 0
        try:
            self.serial = serial.Serial(port,baud)
            print(self.serial)
            print("打开串口成功")
        except:
            self.serial = serial.Serial(port, baud)
            print(self.serial)
            print("打开失串口败")
            self.err = -1
     def uart_recv_threading(self):
         print("开始接收数据")
         while (True):
             try:
                 recv_data_raw=self.serial.readline()
                 data = recv_data_raw[1:-4]
                 print(data)
             except:
                 print("接收失败")
                 break

     def start_recv_threading(self):
         threa=threading.Thread(target=self.uart_recv_threading,daemon=True)
         threa.start()

     def uart_send_data(self,data):
         print("键盘输入的数据：",data)
         self.serial.write(data.encode())

     def uart_close(self):
         self.serial.close()

if __name__ == '__main__':
    myUart=Uart("/dev/cu.wchusbserial14220",115200)
    if myUart.err == 0:
        print("初始化成功")
        myUart.start_recv_threading()
    while (True):
        input_data=input("输入信息:")
        #如果打开串口成功开启线程接收数据
        if input_data == "quit":
            myUart.uart_close()
            break
        else:
            myUart.uart_send_data(input_data)
    print("退出")
    myUart.uart_close()





