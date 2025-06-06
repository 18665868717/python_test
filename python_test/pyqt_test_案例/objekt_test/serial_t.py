import serial
import threading
import datetime
import queue
from time import sleep


class Uart(object):
    def __init__(self, port):
        self.err = 0
        self.run_status = 0
        try:
            self.uart = serial.Serial(port, 9600)
            self.run_status = 1
            print("start uart success")
        except:
            print("start uart error")
            self.err = -1

    def uart_recv_thread(self):
        print("start uart_recv_thread")
        while True:
            try:
                data = self.uart.readline()
                data = "[uart==>pc] " + data.decode()
                print(data)
                sleep(0.05)
            except Exception as e:
                print("Error")
                print(e)

    def run(self):
        threading.Thread(target=self.uart_recv_thread, daemon=True).start()

    def close(self):
        print("close uart")
        self.uart.close()

    def uart_send_data(self, data):
        print("pc==>uart: ", data)
        self.uart.write(data.encode())


if __name__ == "__main__":
    uart = Uart("COM13")
    if (-1 != uart.err):
        uart.run()
    while (True):
        input_data = input("Please input:\r\n")
        if ("quit" == input_data):
            uart.close()
            break
        else:
            uart.uart_send_data(input_data)
        sleep(0.1)
    print("exit uart")