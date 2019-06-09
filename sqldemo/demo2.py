import pymysql


db = pymysql.connect(host='localhost', user='root', password='wujinxing718', port=3306, database='spiders')
cursor = db.cursor()


def demo1():
    '''
    连接成功后，需要再调用cursor()方法获得 MySQL 的操作游标，利用游标来执行SQL语句.
    这里我们执行了两句SQL.直接用execute()方法执行即可,第一句SQL用于获得MySQL的当前版本，
    然后调用fetchone()方法获得第一条数据，也就得到了版本号.第二句SQL执行创建数据库的操作，
    数据库名叫作spiders, 默认编码为UTF-8'''
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version: ', data)
    cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
    db.close()


def demo2():
    sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()


def demo3():
    id = '20190608'
    user = 'Bob'
    age = 20
    sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
    # 标准写法
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
        print("插入完成")
    except:
        db.rollback()   # 执行失败，则调用rollback()执行数据回滚,相当于什么都没有发生过 。
        print("插入失败")
    db.close()


# 动态插入
def demo4():
    data = {
        'id': '20180201',
        'name': 'Bob',
        'age': 20
    }
    table = 'students'
    keys = ','.join(data.keys())    # id,name,age
    values = ','.join(['%s']*len(data))  # %s,%s,%s
    # print(keys, values)
    sql = "INSERT INTO {table}({keys}) values ({values})".format(table=table, keys=keys, values=values)
    # print(sql)          # INSERT INTO students(id,name,age) values (%s,%s,%s)
    # print(tuple(data.values()))     # ('20180201', 'Bob', 20)
    try:
        if cursor.execute(sql, tuple(data.values())):   # 第二个参数传入data的键值构造的元组，
            print("Successful")
            db.commit()
    except:
        print("Failed")
        db.rollback()
    db.close()


# 更新数据
def demo5():
    data = {
        'id': '20180201',
        'name': 'Bob',
        'age': 21
    }
    table = 'students'
    keys = ','.join(data.keys())  # id,name,age
    values = ','.join(['%s'] * len(data))  # %s,%s,%s
    # 加了ON DUPLICATE KEY UPDATE。这行代码的意思是如果主键已经存在，就执行更新操作。
    sql = 'INSERT INTO {table}({keys}) values ({values}) ON DUPLICATE key update'.format(table=table, keys=keys, values=values)
    update = ', '.join([" {key}=%s".format(key=key) for key in data])
    print(sql)      # INSERT INTO students(id,name,age) values (%s,%s,%s) ON DUPLICATE key update
    sql += update
    print(sql)      # INSERT INTO students(id,name,age) values (%s,%s,%s) ON DUPLICATE key update id=%s,  name=%s,  age=%s
    try:
        if cursor.execute(sql, tuple(data.values())*2):
            print("Successful")
            db.commit()
    except:
        print("Failed")
        db.rollback()
    db.close()


# 删除数据
def demo6():
    table = 'students'
    condition = 'age > 20'
    sql = 'DELETE FROM {table} where {condition}'.format(table=table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
        print("Successful")
    except:
        print("Failed")
        db.rollback()
    db.close()


# 查询数据
def demo7():
    sql = 'SELECT * FROM students where  age >= 20'
    try:
        cursor.execute(sql)
        print('Count: ', cursor.rowcount)
        one = cursor.fetchone()
        print('One: ', one)
        results = cursor.fetchall()
        print('Results: ', results)
        print('Results Type: ', type(results))
        for row in results:
            print(row)
    except:
        print('Error')


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    pass