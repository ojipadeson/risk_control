环境要求：
python版本3.7.7
安装graphviz可视化软件（graphviz软件的bin文件添加到系统的环境变量）
从国泰安数据库网站下载csmarapi并解压到python的site-package文件夹
需要安装的python库：
pandas
datetime
math
pydotplus
sklearn
joblib
numpy
matplotlib
prettytable
bayes_opt

***在运行 获取疫情开始时各行业的市场变化数据.py 前，请确保已有国泰安数据库的用户名和密码和已购买“公募基金”数据表的权限，根据竞赛规定，抹去了程序中的用户名和密码，请在自行注册后在程序第20行填入自己的用户名和密码

运行 获得123家有信贷企业的各类指标.py 程序，获得 label123.csv 文件

运行 获得302家有信贷企业的各类指标.py 程序，获得 label302.csv 文件

运行 获取疫情开始时各行业的市场变化数据.py 程序，获得对应代码的ETF数据的csv文件，同时各行业变化率表会保存至trend.csv文件中

运行 依据有信贷企业数据构建信誉评级模型.py 程序，获得评级模型，每次运行模型会自动保存到tree123.pkl，可视化树图片会保存至tree.png

运行 通过训练后的评级模型对无信贷企业进行评级.py，获得无信贷企业的评级数据，保存至predict.csv 文件中

运行 贝叶斯优化的放贷利率策略.py 程序，获得优化放贷策略，依据程序中的模块调整会影响 企业etf修改评级.csv，利率策略.csv两个文件

运行 画图.py 可以按需要获得饼图

运行前请阅读程序注释，并根据需要调整程序中的运行模块。
