'''
将具体数据抽象成数字
'''

from src.function.file_operations import *
import operator

def get_nums():
    topic_count('../../data/analysis/topic_nonPython')
    topic_count('../../data/analysis/topic_testCase')
    user_count('../../data/analysis/user')
    user_count('../../data/analysis/user_effective')

# 在已有字典文件同目录下生成保存各用户做答题数的字典文件
def user_count(root):
    reader = read_json(root + '.json')
    temp = {}
    for user in reader:
        count = 0
        for type in reader[user]:
            count += len(reader[user][type])
        if count>200:
            count = 200
        temp.update({user:count})
    temp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
    generate_json(root + '_num.json', dict(temp))

# 在已有字典文件同目录下生成保存各题无效代码数的字典文件
def topic_count(root):
    reader = read_json(root + '.json')
    temp = {}
    for type in reader:
        count = 0
        for topic in reader[type]:
            count += len(reader[type][topic])
        temp.update({type:count})
    temp = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)
    generate_json(root + '_num.json', dict(temp))