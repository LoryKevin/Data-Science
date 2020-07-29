# 框架设计

## 猜想与选题

根据过往经验和个人体验，猜测同学们在代码中可能普遍存在if-else滥用的问题，包括if...else分支过多以及if...else嵌套过深两种情况。虽然if...else是必需的，但滥用if...else不仅有可能降低程序执行效率，而且会对代码的可读性、可维护性、可拓展性造成很大伤害，进而危害到整个软件系统，不利于团队开发与后期维护。

## 目标

通过分析学生做答及参考答案中if...else使用情况，为已有练习题计算生成if...else分支数及嵌套层数允许使用上限，超出任一限制将会收到提示无法提交。

## 分析方法

### 数据抽取

通过download代码，以题目为单位从源数据中获取学生做答及参考答案数据，保存为.py文件格式

### 数据加载

按照问题情形获得两组所需数据，生成对应的算数平均数、众数、中位数：

1. if...else分支，即：

   ```python
    1 if condition1:
    2     action1()
    3 elif condition2:
    4     action2()
    5 elif condition3:
    6     action3()
    7 elif condition4:
    8     action4()
    9 else:
   10     action5()
   ```

   获得：每份做答及参考答案中同层if...else最大分支数

2. if...else嵌套，即：

   ```python
    1 if condition1:
    2     action1()
    3     if condition2:
    4         action2()
    5         if condition3:
    6             action3()
    7             if condition4:
    8                 action4()
   ```

   获得：每份做答及参考答案中层间if...else最大嵌套数

### 数据可视化

以单一题目为单位生成横轴为最大分支数/最大嵌套数，纵轴为所占百分比的柱状图，

以单一题目为单位生成横轴为最大分支数，纵轴为最大嵌套数的气泡图，分析两变量间是否存在关联

以一组题目为单位生成横轴为题目，纵轴为最大分支数/最大嵌套数的折线图



## 项目结构

- 根目录czy
  - 源文件src
    - 下载文件download：用于通过原始数据将具体数据下载到源数据中
    - 分析文件analysis：用于分析源数据并将分析结果放到分析数据中
    - 功能文件function：用于开发辅助功能简化分析过程
  - 数据data
    - 原始数据origin
    - 元数据source
    - 分析数据analysis
  - 文档doc