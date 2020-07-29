'''
作图
'''

import matplotlib.pyplot as plt
from src.function.file_operations import *

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def graph_generate():
    topic_invalid_barGraph()
    user_num_barGraph()
    user_num_pieChart()

# 生成题目类型-无效代码数堆叠柱形图
def topic_invalid_barGraph():
    nonPython = read_json('../../data/analysis/topic_nonPython_num.json')
    testCase = read_json('../../data/analysis/topic_testCase_num.json')
    type = []
    num_nonPython = []
    num_testCase = [0,1,2,3,4,5,6,7]
    for item in nonPython:
        type.append(item)
        num_nonPython.append(nonPython[item])
    for item in testCase:
        for count in range(0,8):
            if type[count]==item:
                num_testCase[count]=testCase[item]
    bar_nonPython = plt.bar(range(len(type)),num_nonPython,label='非Python代码数', fc='b')
    bar_testCase = plt.bar(range(len(type)),num_testCase, bottom=num_nonPython, label='面向用例编程数', tick_label=type, fc='g')
    pileBar(bar_nonPython,bar_testCase)
    plt.legend()
    # 设置横轴标签
    plt.xlabel('题目类型')
    # 设置纵轴标签
    plt.ylabel('无效代码数')
    # 添加标题
    plt.title('题目类型-无效代码数堆叠柱形图')
    plt.savefig('../../data/image/题目类型-无效代码数堆叠柱形图.png',dpi=300)
    plt.show()

def pileBar(bar1,bar2):
    i = 0
    for column1 in bar1:
        column2 = bar2[i]
        i+=1
        height = column1.get_height() + column2.get_height()
        plt.text(column1.get_x()+column1.get_width()/2. - 0.15, 1.01*height, '%s' % int(height))

def user_num_barGraph():
    section,all,effective = user_num_count()
    x = list(range(len(all)))
    total_width, n = 0.8, 2
    width = total_width / n
    bar_all = plt.bar(x, all, width=width, label='所有提交')
    for column_all in bar_all:
        height = column_all.get_height()
        plt.text(column_all.get_x() + column_all.get_width() / 2. - 0.05, 1.01 * height, '%s' % int(height))
    for i in range(len(x)):
        x[i] += width
    bar_effective = plt.bar(x, effective, width=width, label='有效提交', tick_label=section)
    for column_effective in bar_effective:
        height = column_effective.get_height()
        plt.text(column_effective.get_x() + column_effective.get_width() / 2. - 0.05, 1.01 * height, '%s' % int(height))
    plt.legend()
    # 设置横轴标签
    plt.xlabel('得分/完成题量')
    # 设置纵轴标签
    plt.ylabel('人数')
    # 添加标题
    plt.title('学生得分/完成题量柱形图')
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.savefig('../../data/image/学生得分与完成题量柱形图.png',dpi=300)
    plt.show()

def user_num_pieChart():
    section, all, effective = user_num_count()
    plt.axes(aspect=1)
    plt.pie(x=effective,labels=section,autopct='%3.1f %%')
    plt.title('学生得分/完成题量饼状图')
    plt.savefig('../../data/image/学生得分与完成题量饼状图.png',dpi=300)
    plt.show()

def user_num_count() -> list:
    user_all = read_json('../../data/analysis/user_num.json')
    user_effective = read_json('../../data/analysis/user_effective_num.json')
    section = ['100分\n≥199题','90~99分\n179~198题','80~89分\n159~178题','70~79分\n139~158题','60~69分\n119~138题','0~59分\n≤118题']
    all = [0,0,0,0,0,0]
    effective = [0,0,0,0,0,0]
    for user in user_all:
        num = user_all[user]
        if num>=199:
            all[0]+=1
        elif num>=179:
            all[1]+=1
        elif num>=159:
            all[2]+=1
        elif num>=139:
            all[3]+=1
        elif num>=119:
            all[4]+=1
        else:
            all[5]+=1
    for user in user_effective:
        num = user_effective[user]
        if num>=199:
            effective[0]+=1
        elif num>=179:
            effective[1]+=1
        elif num>=159:
            effective[2]+=1
        elif num>=139:
            effective[3]+=1
        elif num>=119:
            effective[4]+=1
        else:
            effective[5]+=1
    return section,all,effective


