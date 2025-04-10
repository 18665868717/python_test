import socket
import argparse
import sys
import time
#

# parser = argparse.ArgumentParser()
# parser.add_argument('host')
# args = parser.parse_args()
# start = time.time()
#
# try:
#     for port in range(1, 65536):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(1)
#         result = sock.connect_ex((args.host, port))
#
#         if result == 0:
#             # print("Port: {} Open".format(port))
#             info=sock.send(bytes("version"))
#             print(info)
#         sock.close()
# except KeyboardInterrupt:
#     sys.exit()
#
# end = time.time()
# print(f"Scanning completed in: {end - start:.3f}s")
#
# for i in range(1,60000):
#     sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #
# # import nmap
# # def test():
# #     ip = '192.168.1.142'
# #     nm = nmap.PortScanner()
# #     nm.scan(ip, '80, 445', '-v -n -sS -T4 -Pn')
# #     print(nm.command_line())
# #     print(nm.scaninfo())
# #     print(nm.all_hosts())
# #     print(nm[ip])
# #
# #
# #
# # test()
from datetime import datetime
from threading import Timer

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.3.37',6666))
def aha_shei():
    str = 'this is test'

    str = str.encode("utf-8")
    s.send(str)

while True:
    # str = 'this is test'
    #
    # str = str.encode()


# s.send('shei')
# s.close()
    def aa():
        aha_shei()
        t = Timer(3,aa )
        t.start()
    aa()


    print(s.recv(1024).decode('utf-8'))



# def pr_shei():
#     print("定时任务")
# def task():
#     now = datetime.now()
#     ts = now.strftime("%Y-%m-%d %H:%M:%S")
#     print(ts)
#
#
# def func():
#     pr_shei()
#     t = Timer(3, func)
#     t.start()
#
#
# func()