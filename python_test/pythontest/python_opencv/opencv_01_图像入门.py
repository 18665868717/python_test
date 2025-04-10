import numpy  as np
import cv2 as cv



""" cv.imread() 函数读取一张图像"""
"""用 cv.imshow() 函数在窗口中显示图像，窗口自动适应图像的大小。"""
img=cv.imread("./6411714986231_.pic.jpg",-1)
cv.imshow("图像",img)  #显示图像  title ｜  图像文件名
cv.waitKey(0)    #是一个键盘绑定函数，它的参数是以毫秒为单位的时间。监听键盘时间，有事件后立即退出
cv.destroyAllWindows()  #简单的销毁我们创建的所有窗口。如果你想销毁任意指定窗口，应该使用函数 cv.destroyWindow() 参数是确切的窗口名。

# cv.namedWindow('image', cv.WINDOW_NORMAL) #有一种特殊情况，你可以先创建一个窗口然后加载图像到该窗口。在这种情况下，你能指定窗口是否可调整大小。它是由这个函数完成的 **cv.namedWindow()**。默认情况下，flag 是 **cv.WINDOW_AUTOSIZE**。但如果你指定了 flag 为 **cv.WINDOW_NORMAL**，你能调整窗口大小。当图像尺寸太大，在窗口中添加跟踪条是很有用的。
# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()



"""
        保存图像，用这个函数 **cv.imwrite()**。
下面的程序以灰度模式读取图像，显示图像，如果你按下 's‘ 会保存和退出图像，或者按下 ESC 退出不保存。

"""

img = cv.imread('messi5.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27: # ESC 退出
    cv.destroyAllWindows()
elif k == ord('s'): # 's' 保存退出
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()