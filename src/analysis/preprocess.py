'''
在分析前对源文件进行预处理
'''

from src.function.iterator import *
from src.function.file_operations import *
import os
import shutil

# 数据预处理
def data_preprocess():
    print("    数据预处理开始！")
    topic_preprocess()
    user_preprocess()
    print("    数据预处理完成！")

def topic_preprocess():
    generate_json('../../data/analysis/topic.json', topic_dictionary_generate()) # 字典目录文件dictionary_topic.json
    topic_check()
    generate_json('../../data/analysis/topic.json', topic_dictionary_generate()) # 重新生成删除错误目录后的字典文件

def user_preprocess():
    generate_json('../../data/analysis/user.json', user_dictionary_generate()) # 字典目录文件dictionary_user.json
    user_check()
    generate_json('../../data/analysis/user.json', user_dictionary_generate()) # 重新生成删除错误目录后的字典文件

# 生成按题目分类目录的字典文件
def topic_dictionary_generate() -> dict:
    result = {}
    topic_type = os.listdir('../../data/source/题目分析')
    if '.DS_Store' in topic_type:
        topic_type.remove('.DS_Store')

    for type in topic_type:
        result[type] = {}
        topics = os.listdir('../../data/source/题目分析/' + type)
        if '.DS_Store' in topics:
            topics.remove('.DS_Store')

        for topic in topics:
            users = os.listdir('../../data/source/题目分析/' + type + '/' + topic)
            if '.DS_Store' in users:
                users.remove('.DS_Store')
            if not users:
                os.rmdir('../../data/source/题目分析/' + type + '/' + topic)
            else:
                result[type][topic] = users
    return result

# 生成按用户分类目录的字典文件
def user_dictionary_generate() -> dict:
    result = {}
    users = os.listdir('../../data/source/用户分析')
    if '.DS_Store' in users:
        users.remove('.DS_Store')
    for user in users:
        result[user] = {}
        types = os.listdir('../../data/source/用户分析/' + user)
        if '.DS_Store' in types:
            types.remove('.DS_Store')
        for type in types:
            topics = os.listdir('../../data/source/用户分析/' + user + '/' + type)
            if '.DS_Store' in topics:
                topics.remove('.DS_Store')
            if not topics:
                os.rmdir('../../data/source/用户分析/' + user + '/' + type)
            else:
                result[user][type] = topics
    return result

# 遍历检查下载内容是否被正确处理
def topic_check():
    it = getTIterator()
    while it.next():
        try:
            if it.get_type() != '.DS_Store' and it.get_user() != '.DS_Store' and it.get_topic() != '.DS_Store':
                docs = os.listdir('../../data/source/题目分析/' + it.get_type() + '/' + it.get_topic() + '/' + it.get_user())
                # 检查目录内容是否为解压内容
                assert docs.index('.mooctest') != -1
                assert docs.index('blockly.xml') != -1
                assert docs.index('main.py') != -1
                assert docs.index('properties') != -1
                assert docs.index('readme.md') != -1
        except ValueError:
            print()
            print(it.get_type() + '/' + it.get_topic() + '/' + it.get_user())
            shutil.rmtree('../../data/source/题目分析/' + it.get_type() + '/' + it.get_topic() + '/' + it.get_user()) # 删除错误目录

def user_check():
    it = getUIterator()
    while it.next():
        try:
            if it.get_type() != '.DS_Store' and it.get_user() != '.DS_Store' and it.get_topic() != '.DS_Store':
                docs = os.listdir('../../data/source/用户分析/' + it.get_user() + '/' + it.get_type() + '/' + it.get_topic())
                assert docs.index('.mooctest') != -1
                assert docs.index('blockly.xml') != -1
                assert docs.index('main.py') != -1
                assert docs.index('properties') != -1
                assert docs.index('readme.md') != -1
        except ValueError:
            print()
            print(it.get_user() + '/' + it.get_type() + '/' + it.get_topic())
            shutil.rmtree('../../data/source/用户分析/' + it.get_user() + '/' + it.get_type() + '/' + it.get_topic()) # 删除错误目录