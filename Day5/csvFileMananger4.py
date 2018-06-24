import csv

import os


class CsvFileManager:
    @classmethod
    def read(self,filename):
        list = []  #声明一个空列表
        # 这是一个固定写法 用来获取当前文件的目录结构
        # os表示操作系统，path路径，dirname目录名，__file__是py的内置对象，表示当前文件
        # 用base_Path的好处：不管文件放在任何路径下，都可以找到该文件的绝对路径
        base_path = os.path.dirname(__file__)
        print(base_path)
        #那么如何找到csv文件的路径
        # 可以通过basepath推算出csv文件的路径
        path = base_path.replace('Day5','data/'+filename)
        print(path)
        # date = r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_date.csv'
        # file = open(path,'r')
        with open(path,'r') as file:
            date_table = csv.reader(file)
            # 遍历
            for row in  date_table:
                print(row)
#        打印不是目的，使用这些数据进行测试才是目的
#       所以就需要给方法设置返回值，把数据提取出来
#       5.声明一个二维列表，保存data_table中的所有数据
                list.append(row)
#         在read方法末尾，返回这个列表
        return list
if __name__ == '__main__':
    list = CsvFileManager().read('test_date.csv')
    print(list)