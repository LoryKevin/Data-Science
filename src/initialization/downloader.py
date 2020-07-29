'''
提供两种源数据下载方法接口
'''

import json
import urllib.request, urllib.parse
import os
import zipfile
from src.initialization.generator import *

def data_initialize():
    print("    数据初始化开始！")
    dir_generate()
    print("        源数据下载开始！")
    work_path = '../../data/source/题目分析'
    if not os.listdir(work_path):
        topic_download()
    work_path = '../../data/source/用户分析'
    if not os.listdir(work_path):
        user_download()
    print("        源数据下载完成！")
    print("    数据初始化完成！")

#按题目为单位下载源数据
def topic_download():
    f = open('../../data/origin/test_data.json', encoding='utf-8')  # 打开'test_data.json'的json文件
    res = f.read()
    data = json.loads(res)  # 加载json数据
    indexes = list(data)
    # 遍历做题信息
    directory = "../../data/source/题目分析/"
    for index in indexes:
        cases = data[index]['cases']
        user_id = 'user_id_' + index
        for case in cases:
            case_id = case['case_id']
            case_type = case['case_type']
            final_score = case['final_score']
            upload_records = sorted(case["upload_records"], key=lambda x: x["score"], reverse=True)
            try:
                upload_record = upload_records[0]
            except IndexError:
                continue
            upload_id = upload_record["upload_id"]
            upload_time = upload_record["upload_time"]
            code_url = upload_record["code_url"]
            name = urllib.parse.unquote(os.path.basename(case["case_zip"]))

            if "*" in name:
                name = name.replace("*", "_")
            try:
                os.mkdir(directory + case_type)
            except FileExistsError:
                pass
            try:
                os.mkdir(directory + case_type + '/' + name[:len(name) - 4])
            except FileExistsError:
                pass
            try:
                os.mkdir(directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id)
            except FileExistsError:
                if not os.listdir(directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id):
                    pass
                else:
                    continue

            filename = directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id + '/' + name
            print('        '+filename)
            urllib.request.urlretrieve(code_url, filename)  # 下载题目包到本地

            try:
                zf_1 = zipfile.ZipFile(filename)
                zf_1.extractall(path=directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id)
                zf_1.close()
                os.remove(filename)
            except RuntimeError as e:
                print(e)
            except zipfile.BadZipfile:
                pass

            filename = directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id + "/" + \
                       os.listdir(directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id)[0]
            try:
                zf_2 = zipfile.ZipFile(filename)
                zf_2.extractall(path=directory + case_type + '/' + name[:len(name) - 4] + '/' + user_id)
                zf_2.close()
                os.remove(filename)
            except RuntimeError as e:
                print(e)
            except zipfile.BadZipfile or FileNotFoundError:
                pass

# 以用户为单位下载源数据
def user_download():
    f = open('../../data/origin/test_data.json', encoding='utf-8')  # 打开'test_data.json'的json文件
    res = f.read()
    data = json.loads(res)  # 加载json数据
    indexes = list(data)
    # 遍历做题信息
    directory = "../../data/source/用户分析/"
    for index in indexes:
        cases = data[index]['cases']
        user_id = 'user_id_' + index
        for case in cases:
            case_id = case['case_id']
            case_type = case['case_type']
            final_score = case['final_score']
            upload_records = sorted(case['upload_records'], key=lambda x: x['upload_id'], reverse=True)
            try:
                upload_record = upload_records[0]
            except IndexError:
                continue
            upload_id = upload_record["upload_id"]
            upload_time = upload_record["upload_time"]
            code_url = upload_record["code_url"]
            name = urllib.parse.unquote(os.path.basename(case["case_zip"]))  # 获取文件名，ur1里对中文会urlencode,解个码

            if "*" in name:
                name = name.replace("*", "_")
            try:
                os.mkdir(directory + user_id)
            except FileExistsError:
                pass
            try:
                os.mkdir(directory + user_id + '/' + case_type)
            except FileExistsError:
                pass
            try:
                os.mkdir(directory + user_id + '/' + case_type + '/' + name[:len(name) - 4])
            except FileExistsError:
                if not os.listdir(directory + user_id + '/' + case_type + '/' + name[:len(name) - 4]):
                    pass
                else:
                    continue

            filename = directory + user_id + '/' + case_type + '/' + name[:len(name) - 4] + '/' + name
            print(filename)
            urllib.request.urlretrieve(code_url, filename)  # 下载题目包到本地

            try:
                zf_1 = zipfile.ZipFile(filename)
                zf_1.extractall(path=directory + user_id + '/' + case_type + '/' + name[:len(name) - 4])
                zf_1.close()
                os.remove(filename)
            except RuntimeError as e:
                print(e)
            except zipfile.BadZipfile:
                pass

            filename = directory + user_id + '/' + case_type + '/' + name[:len(name) - 4] + '/' + \
                       os.listdir(directory + user_id + '/' + case_type + '/' + name[:len(name) - 4])[0]
            try:
                zf_2 = zipfile.ZipFile(filename)
                zf_2.extractall(path=directory + user_id + '/' + case_type + '/' + name[:len(name) - 4])
                zf_2.close()
                os.remove(filename)
            except RuntimeError as e:
                print(e)
            except zipfile.BadZipfile or FileNotFoundError:
                pass