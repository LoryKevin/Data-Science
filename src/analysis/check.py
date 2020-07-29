'''
代码检查
'''

from src.function.iterator import *
from src.function.file_operations import *

def code_check():
    print("    代码检查开始！")
    check_nonPython()
    check_testCase()
    print("    代码检查完成！")

# 检查非Python代码
def check_nonPython():
    print("        非Python代码检查开始！")
    non_python = {}
    it = getUIterator()
    while it.next():
        if user_nonPython(it):
            add_Uindex(non_python, it)
    generate_json('../../data/analysis/user_nonPython.json', non_python) # 生成按用户为单位的非Python代码目录的字典文件
    non_python = {}
    it = getTIterator()
    while it.next():
        if topic_nonPython(it):
            add_Tindex(non_python, it)
    generate_json('../../data/analysis/topic_nonPython.json', non_python) # 生成按题目为单位的非Python代码目录的字典文件
    print("        非Python代码检查完成！")

def user_nonPython(it):
    user = it.get_user()
    type = it.get_type()
    topic = it.get_topic()
    root = user + '/' + type + '/' + topic + '/properties'
    properties = read_json('../../data/source/用户分析/' + root)
    if properties['lang'] == 'Python':
        return False
    elif properties['lang'] == 'Python3':
        return False
    else:
        return True

def topic_nonPython(it):
    type = it.get_type()
    topic = it.get_topic()
    user = it.get_user()
    root = type + '/' + topic + '/' + user + '/properties'
    properties = read_json('../../data/source/题目分析/' + root)
    if properties['lang'] == 'Python':
        return False
    elif properties['lang'] == 'Python3':
        return False
    else:
        return True

# 检查面向测试用例编程
def check_testCase():
    print("        面向用例编程检查开始！")
    test_oriented = user_testCase(find_topic())
    generate_json('../../data/analysis/user_testCase.json', test_oriented) # 生成按用户为单位的面向用例代码目录的字典文件
    test_oriented = topic_testCase(find_topic())
    generate_json('../../data/analysis/topic_testCase.json', test_oriented) # 生成按题目为单位的面向用例代码目录的字典文件
    print("        面向用例编程检查完成！")

def user_testCase(topic_list: dict) -> dict:
    test_cases = read_json('../../data/analysis/test_cases.json')
    result = {}
    for item in test_cases.items():
        if item[1] is not []:
            users = item[1]
            for user in users:
                if 'user_id_' + user in list(result.keys()):
                    pass
                else:
                    result['user_id_' + user] = {}
                type, topic = topic_list[item[0]].split('/')
                if type in list(result['user_id_' + user].keys()):
                    pass
                else:
                    result['user_id_' + user][type] = []
                if topic in result['user_id_' + user][type]:
                    pass
                else:
                    result['user_id_' + user][type].append(topic)
    return result

def topic_testCase(topic_list: dict) -> dict:
    test_cases = read_json('../../data/analysis/test_cases.json')
    result = {}
    for item in test_cases.items():
        type, topic = topic_list[item[0]].split('/')
        if type in list(result.keys()):
            pass
        else:
            result[type] = {}
        result[type][topic] = []
        users = item[1]
        for user in users:
            result[type][topic].append('user_id_' + user)
    return result

def find_topic() -> dict:
    test_data = read_json('../../data/origin/test_data.json')
    result = {}
    for item in test_data.items():
        cases = dict(item[1])
        for case in cases['cases']:
            if case['case_id'] in list(result.keys()):
                continue
            else:
                type = case['case_type']
                topic = case['case_zip'].split('/')[4]
                topic = topic[:len(topic) - 4]
                topic = topic.replace('*', '_')
                result[case['case_id']] = type + '/' + topic
    return result