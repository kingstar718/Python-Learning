import pymysql


def demo1():
    db = pymysql.connect(host='localhost', user='root', password='wujinxing718', port=3306)
    '''
    连接成功后，需要再调用cursor()方法获得 MySQL 的操作游标，利用游标来执行SQL语句.
    这里我们执行了两句SQL.直接用execute()方法执行即可,第一句SQL用于获得MySQL的当前版本，
    然后调用fetchone()方法获得第一条数据，也就得到了版本号.第二句SQL执行创建数据库的操作，
    数据库名叫作spiders, 默认编码为UTF-8'''
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version: ', data)
    cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
    db.close()


def demo2():
    db = pymysql.connect(host='localhost', user='root', password='wujinxing718', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()


def demo3():
    id = '20190608'
    user = 'Bob'
    age = 20
    db = pymysql.connect(host='localhost', user='root', password='wujinxing718', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
    # 标准写法
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
        print("插入完成")
    except:
        db.rollback()
        print("插入失败")
    db.close()


if __name__ == "__main__":
    # demo1()
    # demo2()
    demo3()
    pass