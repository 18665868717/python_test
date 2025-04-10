#
# import re
# import matplotlib.pyplot as plt
#
#
# azimuth=[]
# elevation=[]
#
# dict0={}
# dict_sort={}
# dict_result={}
#
# data=[]
# filter_result=[]
# azimuth_degree=[]
# azimuth_list=[]
# azimuth_x=[]
# elevation_list=[]
# elevation_x=[]
# elevation_degree=[]
#
# expression_01=r'^id:R:FD:AB:79:08:EE:72.(azimuth:\d[1-9]{0,3}).elevation.\d[1-9]{1,3}'
# expression_02=r'^id:R:FD:AB:79:08:EE:72.azimuth:\d[1-9]{0,3}.(elevation.\d[1-9]{1,3})'
# result={}
# # azimuth_list=[32,33]
# # azimuth_degree=[33, 496]
# def read_txt_file():
#     with open('./45°方向上不同距离的角度偏差/45°方向(距离约1M).txt',encoding="utf-8",mode="r")as f:
#         content=f.readlines()
#         return content
#
# def fitter_data(content):
#     for i in content:
#         # print(i)
#         data_azimuth=re.search(expression_01,i,re.M|re.I)
#         data_elevation=re.search(expression_02,i,re.M|re.I)
#
#         if data_azimuth != None or data_elevation != None:
#             # print(id_data)id_data
#             azimuth.append(data_azimuth.groups(0))
#             elevation.append(data_elevation.groups(0))
#
#
# def wiret_dict():
#     for i in azimuth:
#         if i in dict0:
#             dict0[i]+=1
#         else:
#             dict0[i]=1
#
#     # def
# def part_key_value():
#     # print(dict_result)
#     # print()
#     # dict_sort = dict(dict_sort)
#     for key,value in dict0.items():
#         # print(key,value)
#         azimuth_list.append(key)
#         azimuth_degree.append(value)
#
# def del_index():
#     for i in azimuth_list:
#         data=list(i)
#         # data.remove('azimuth:')
#         for m in data:
#             m=m.split(':')
#             azimuth_x.append(m[1])
#
#
# def drawing_image():
#     #
#     # plt.rcParams["font.sans-serif"] = ["SimHei"]
#     # plt.rcParams["axes.unicode_minus"] = False
#
#     for i in range(len(azimuth_list)):
#         plt.bar(, azimuth_degree[i])
#     # 设置图片名称
#     plt.title("angle_analyse")
#     # 设置x轴标签名
#     plt.xlabel("azimuth")
#     # 设置y轴标签名
#     plt.ylabel("count")
#     # 显示
#     plt.show()
#
# def key_sort():
#
#     for i in sorted(data_key):
#         # print(type(i))
#         # global result
#         # result[i]= dict0[i]
#         print ((i, data_key[i]), end =" ")
#
#         # print(result)
# if __name__ == '__main__':
#     biaoda=":\d{0,3}"
#     zidian={}
#     content=read_txt_file()
#     fitter_data(content)
#     # print(azimuth)
#     # print(elevation)
#
#     wiret_dict()  #统计次数写入dict
#     # print(azimuth)
#
#     for i in azimuth:
#         i=str(i)
#         # print(i)
#         result=re.match(biaoda,i,re.M|re.I)
#         print(result)
#
#         if result in zidian:
#             zidian[i] += 1
#         else:
#             zidian[i] = 1
#     print(zidian)
#     # data_key=dict(dict0)
#     # print(data_key)
#     # print(type(data_key))
#
#     # list1 = sorted(data_key.items(), key=lambda x: x[1])
#     #
#     # print(list1)
#     # # key_sort(data_key)
#     # # print(result)
#     # # print(dict_sort)
#     # # print(dict_sort)
#     # # print(dict(dict_sort))
#     part_key_value() #将字典的键值对分开
#     # # print(elevation_list)
#     # del_index()
#     #
#
#     drawing_image()
#
#
import random
import string
"""随机生成字符串"""

client_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
print(client_id)

s1='-'
s2=''
seq1=("r","u","n","o")
print(s1.join(seq1))
print(s2.join(seq1))

"""列表推导式"""
ls1=['bu','zhi','dao','liu','yang']
print([i**2 for i in range(0,9)])
print([i for i in ls1 if len(i)>=3])

"""三目运算"""
a=10
b=5
c= a-b if a > b else b-a
print(c)

"""lambda 表达式   匿名函数"""
add=lambda a,y:a+y
print(add(7,3))

"""*args, **kwargs 使用讲解"""
"""装饰器"""

"""Python装饰器是Python语言中一种特殊的语法结构，可以在不修改原函数源码的情况下，对原函数进行功能扩展或修饰。装饰器本质上是一个可调用的对象，它可以接受一个函数作为输入，并返回一个新的函数作为输出。

装饰器在Python中通常用于实现横切关注点（cross-cutting concern）的功能，例如日志记录、性能分析、鉴权等。它能够将这些功能逻辑与业务逻辑分离，使得代码更加清晰、简洁和可维护。

下面是一个简单的装饰器示例：

```Python"""
def decorator(func):
    def wrapper(*args, **kwargs):
        # 对原函数进行修饰扩展的代码
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@decorator
def foo():
    print("Inside the function")

foo()
"""

在上面的例子中，`decorator`是一个装饰器函数，它接受一个函数作为参数。`wrapper`函数是一个内部函数，它承担了对原函数进行修饰扩展的任务。`@decorator`语法糖将装饰器应用到`foo`函数上。
当调用`foo`函数时，实际上执行的是经过装饰器修饰后的`wrapper`函数。在调用原函数之前，`wrapper`函数会输出"Before calling the function"，然后调用原函数，输出"Inside the function"，最后输出"After calling the function"。
装饰器可以接受参数，实现更加灵活的功能扩展。可以通过外层的装饰器函数来接受参数，并返回一个内层的装饰器函数。以下是一个带参数的装饰器示例：Python
"""
# def decorator_with_args(arg1, arg2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # 对原函数进行修饰扩展的代码
#             print(f"arg1: {arg1}, arg2: {arg2}")
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @decorator_with_args("Hello", "World")
# def bar():
#     print("Inside the function")
#
# bar()
"""
在上面的例子中，`decorator_with_args`是一个装饰器函数，它接受两个参数`arg1`和`arg2`。内部定义了一个装饰器函数`decorator`，它接受一个函数作为参数，并返回一个装饰后的函数。`wrapper`函数依然承担了对原函数进行修饰扩展的任务。
当调用`bar`函数时，实际上执行的是经过装饰器修饰后的`wrapper`函数。在调用原函数之前，`wrapper`函数会输出"arg1: Hello, arg2: World"，然后调用原函数，输出"Inside the function"。
总结来说，装饰器是一种强大的Python特性，能够在不修改原函数源码的情况下，对函数进行功能扩展或修饰。通过使用装饰器可以实现代码的重用和解耦，提高代码的可维护性和可读性。
"""

"""闭包函数"""