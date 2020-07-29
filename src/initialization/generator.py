'''
预先生成数据区所需文件系统
'''

import os

# 生成数据区目录
def dir_generate():
    print("        数据区目录生成开始！")
    try:
        os.mkdir('../../data') # 数据区总目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/origin') # 原始数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/source') # 源数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/analysis') # 分析中间数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/image') # 分析结果图形数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/source/题目分析') # 按题目分类的源数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/source/用户分析') # 按用户分类的源数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/source/无效代码') # 无效代码数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/source/无效代码/题目分析') # 按题目分类的无效代码数据目录
    except FileExistsError:
        pass
    try:
        os.mkdir('../../data/source/无效代码/用户分析') # 按用户分类的源数据目录
    except FileExistsError:
        pass
    print("        数据区目录生成完成！")