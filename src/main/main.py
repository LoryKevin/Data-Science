from src.initialization.downloader import *
from src.analysis.preprocess import data_preprocess
from src.analysis.check import *
from src.analysis.remove import *
from src.visualization.count import *
from src.visualization.plot import *

if __name__ == '__main__':
    print("分析开始！")
    data_initialize() # 数据初始化，包括文件系统初始化、下载源数据
    data_preprocess() # 数据预处理，包括检查数据下载情况、生成字典文件
    code_check() # 代码检查，包括面向用例编程和非Python代码检查
    code_remove() # 代码移除，将无效代码移至专门文件夹
    get_nums() # 频数计数，按题目或用户为单位计算多个频数
    graph_generate() # 图像生成，绘制统计图
    print("分析完成！")

