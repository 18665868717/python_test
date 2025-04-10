# import matplotlib.pyplot as plt
#
# x_data = [10,20,30,40,50]
# y_data = [10,10,30,40,50]
# for i in range(len(x_data)):
# 	plt.bar(x_data[i], y_data[i])
# # 设置图片名称
# plt.title("销量分析")
# # 设置x轴标签名
# plt.xlabel("年份")
# # 设置y轴标签名
# plt.ylabel("销量")
# # 显示
# plt.show()
import re

import re
import matplotlib.pyplot as plt

azimuth=[]
elevation=[]

dict0={}


azimuth_x=[]
elevation_x=[]

expression_01=r'^id:R:FD:AB:79:08:EE:72.azimuth:(\d[1-9]{0,3}).elevation.\d[1-9]{1,3}'
expression_02=r'^id:R:FD:AB:79:08:EE:72.azimuth:\d[1-9]{0,3}.elevation.(\d[1-9]{1,3})'
result={}
# azimuth_list=[32,33]
# azimuth_degree=[33, 496]
elevation_list=[]
elevation_degree=[]

azimuth_list=[]
azimuth_degree=[]
def read_txt_file():
    with open('./45°方向上不同距离的角度偏差/45°方向(距离约1M).txt',encoding="utf-8",mode="r")as f:
        content=f.readlines()
        # print(content)
        return content

def fitter_data(content):
    for i in content:
        # print(i)
        data_azimuth=re.search(expression_01,i,re.M)
        data_elevation=re.search(expression_02,i,re.I)
        # print(data_elevation)

        if data_azimuth != None or data_elevation != None:
            azimuth_x.append(data_azimuth.group(1))
            elevation_x.append(data_elevation.group(1))
            # print(data_elevation)
            # print(data_azimuth)
            # azimuth.append(data_azimuth.groups(0))
            # elevation.append(data_elevation.groups(0))

def wiret_dict():
    for i in azimuth_x:
        if i in dict0:
            dict0[i]+=1
        else:
            dict0[i]=1

def part_key_value():
    # print(dict_result)
    # print()
    # dict_sort = dict(dict_sort)
    for key,value in data_result.items():
        # print(key,value)

        azimuth_list.append(key)
        azimuth_degree.append(value)
    print(data_result)
def drawing_image():
    #
    # plt.rcParams["font.sans-serif"] = ["SimHei"]
    # plt.rcParams["axes.unicode_minus"] = False

    for i in range(len(azimuth_list)):
        plt.bar(azimuth_list[i],azimuth_degree[i])
    # 设置图片名称
    for a, b, i in zip(azimuth_list, azimuth_degree, range(len(azimuth_list))):  # zip 函数
        plt.text(a, b+ 10, "%.2f" % azimuth_list[i], ha='center', fontsize=7)
        plt.axhline(azimuth_degree[i], ls='--', c='red',xmin=10)
    plt.title("angle_analyse")
    # 设置x轴标签名
    plt.xlabel("azimuth")
    # 设置y轴标签名
    plt.ylabel("count")
    # 显示
    plt.show()

if __name__ == '__main__':
    connect=read_txt_file()
    fitter_data(connect)
    new_li = []
    for i in azimuth_x:
        i =int(i)

        new_li.append(i)

    new_li.sort(key=None,reverse=False)

    data_result={}

    for i in new_li:
        print(i)
        if i in data_result:
            data_result[i] += 1
        else:
            data_result[i] = 1

    part_key_value()

    drawing_image()

