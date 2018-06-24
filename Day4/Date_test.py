import csv
# 如果要读取excel需要下载相应的代码库：xlrd
# 怎么下载：1.通过命令下载：在dos窗口中，输入pip install -U xlrd
# selenium可以通过selenium包下载，也可以通过命令下载：pip install selenium/pip3 install selenium
# -U是升级到最新版的意思
# pip是python语言最常用的项目管理工具，和JAVA中的maven类似
path=r'C:\Users\51Testing\PycharmProjects\selenium7th\date\test_date.csv'
#因为字符串中包含反斜线\t等
print(path)
file = open(path,'r')
date_table = csv.reader(file)
for item in date_table:
    print(item)