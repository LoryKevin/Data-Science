from src.initialization.downloader import *
from src.analysis.preprocess import data_preprocess
from src.analysis.check import *
from src.analysis.remove import *

if __name__ == '__main__':
    print("分析开始！")
    data_initialize()
    data_preprocess()
    code_check()
    code_remove()
    print("分析完成！")

