import json

# 收集迭代器中的数据以便生成符合用户分析的迭代文件
def add_Uindex(result, it):
    if it.get_user() not in list(result):
        result[it.get_user()] = {it.get_type(): [it.get_topic()]}
    elif it.get_type() not in list(result[it.get_user()]):
        result[it.get_user()][it.get_type()] = [it.get_topic()]
    else:
        result[it.get_user()][it.get_type()].append(it.get_topic())

# 收集迭代器中的数据以便生成符合题目分析的迭代文件
def add_Tindex(result, it):
    if it.get_type() not in list(result):
        result[it.get_type()] = {it.get_topic(): [it.get_user()]}
    elif it.get_topic() not in list(result[it.get_type()]):
        result[it.get_type()][it.get_topic()] = [it.get_user()]
    else:
        result[it.get_type()][it.get_topic()].append(it.get_user())

# 生成json文件
def generate_json(root, data):
    json_data = json.dumps(data, indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open(root, 'w', encoding='utf-8')
    f.write(json_data)
    f.close()

# 读取json文件
def read_json(root) -> dict:
    file = open(root, 'r', encoding='utf-8')
    res = file.read()
    data = json.loads(res)
    return data

# 读取普通文件
def read_file(root) -> str:
    file = open(root, 'r', encoding='utf-8')
    return file.read()

# 按行读取普通文件
def read_filelines(root) -> []:
    file = open(root, 'r', encoding='utf-8')
    result = file.readlines()
    return result