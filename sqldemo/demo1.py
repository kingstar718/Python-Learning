# -*- coding: UTF-8 -*-

import MySQLdb

conn = MySQLdb.connect(host = '127.0.0.1', port=3306,user='root',passwd='wujinxing718'
                       ,db = 'mydb1',charset='utf8')
cursor = conn.cursor()
print(conn)
print(cursor)

cursor.execute("""
create table if not EXISTS user
(
  userid int(11) PRIMARY KEY ,
  username VARCHAR(20)
)
""")

for i in range(1,10):
    cursor.execute("insert into user(userid,username) values('%d','%s')" % (int(i), 'name' + str(i)))

conn.autocommit()
cursor.close()
conn.cursor()