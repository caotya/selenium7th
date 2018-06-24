# 下载并导入代码库：py mysql
#
import pymysql


class DBconnection:
    def ececute_sql_command(self):
       conn =  pymysql.Connect(host='127.0.0.1', user='root', password="root",
                 database='pirate', port=3306,
                 charset='utf8')
       try:
           cursor = conn.cursor()
           sql = 'select * from hd_user order by id desc;'
           cursor.execute(sql)
           all_result = cursor.fetchall()
           for row in  all_result:
               return row
           conn.commit()
       finally:
           conn.close()

if __name__ == '__main__':
    DBconnection().ececute_sql_command()