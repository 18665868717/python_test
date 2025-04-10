import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_excel("data - 1.xlsx")  # 从文件夹提取我们需要的内容
# print(df1)   #打印出来看看
date = df1['日期']  # 提取的抬头
y1 = df1['新增确诊人数']
y2 = df1['新增无症状人数']
y3 = df1['治愈人数']

date = ['2022年3月4日', '2022年3月5日', '2022年3月6日', '2022年3月7日',
        '2022年3月8日', '2022年3月9日', '2022年3月10日', '2022年3月11日', '2022年3月12日',
        '2022年3月13日', '2022年3月14日', '2022年3月15日', '2022年3月16日', '2022年3月17日',
        '2022年3月18日', '2022年3月19日', '2022年3月20日', '2022年3月21日',
        '2022年3月22日', '2022年3月23日', '2022年3月24日', '2022年3月25日', '2022年3月26日', '2022年3月27日',
        '2022年3月28日', '2022年3月29日', '2022年3月30日', '2022年3月31日', '2022年4月1日'
    , '2022年4月2日', '2022年4月3日', '2022年4月4日'
    , '2022年4月5日', '2022年4月6日', '2022年4月7日']
print(len(date))
y1 = list(y1)
y2 = list(y2)
y3 = list(y3)
print(y1)
print(y2)
print(y3)

plt.rcParams["font.sans-serif"] = ['SimHei']  # 方便汉语
plt.rcParams["axes.unicode_minus"] = False
plt.figure()

for i in range(35):  # 动态的意义是延时输出图片
    plt.cla()  # 清除当前的图片，重新画新的
    title = ['新增确诊人数', '新增无症状人数']

    p1 = plt.bar(title[0], y1[i], width=0.3, color='lightcoral')  # 标题的设置
    p2 = plt.bar(title[1], y2[i], width=0.3, color='turquoise')

    plt.bar_label(p1, label_type='edge', fontsize=12)  # 柱状图上面的小标题
    plt.bar_label(p2, label_type='edge', fontsize=12)
    plt.title(date[i], fontsize=20)  # 柱状图上面的大标题
    plt.ylim(0, 1000)  # 坐标

    if y1[i] > 1000 or y2[i] > 1000:  # 老师让做动态坐标，在播放的过程中坐标会发生变化
        plt.ylim(0, 21000)
    else:
        plt.ylim(0, 1000)
    # plt.ylabel("新增人数", fontsize=20)
    plt.xticks(fontsize=10)

    plt.pause(0.1)  # 延时，每次图片播放的时间填多少就是多少，单位为秒
plt.show()