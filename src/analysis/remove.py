'''
移除无效代码
'''

import shutil
from src.analysis.preprocess import topic_dictionary_generate,user_dictionary_generate
from src.function.iterator import *
from src.function.file_operations import *

def code_remove():
    print("    移除无效代码开始！")
    remove_invalid(UIterator('../../data/analysis/user_nonPython.json'))
    remove_invalid(UIterator('../../data/analysis/user_testCase.json'))
    generate_json('../../data/analysis/topic_effective.json', topic_dictionary_generate())
    generate_json('../../data/analysis/user_effective.json', user_dictionary_generate())
    print("    移除无效代码完成！")


def remove_invalid(it):
    while it.next():
        src_1 = '../../data/source/用户分析/' + it.get_user() + '/' + it.get_type() + '/' + it.get_topic()
        dst_1 = '../../data/source/无效代码/用户分析/' + it.get_user() + '/' + it.get_type() + '/' + it.get_topic()
        src_2 = '../../data/source/题目分析/' + it.get_type() + '/' + it.get_topic() + '/' + it.get_user()
        dst_2 = '../../data/source/无效代码/题目分析/' + it.get_type() + '/' + it.get_topic() + '/' + it.get_user()
        try:
            shutil.move(src_1, dst_1)
            shutil.move(src_2, dst_2)
        except FileNotFoundError:
            continue