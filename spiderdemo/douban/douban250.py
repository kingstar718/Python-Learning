from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import json
import pymysql


def get_bs(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, features="lxml")
    return bsObj


def get_content(bsObj):
    bookList = []

    for i in bsObj.find_all(name='tr', attrs={'class': 'item'}):
        bookDirt = {}
        bookDirt['bookName'] = i.div.a['title']
        bookDirt['bookAddress'] = i.td.a['href']
        bookDirt['bookImg'] = i.td.a.img['src']
        bookDirt['bookAuthor'] = i.p.string

        # bookDirt['bookConculsion'] = i.find_all('span', attrs={'class': 'inq'})[0].string
        bookDirt['bookScore'] = i.find_all('span', attrs={'class': 'rating_nums'})[0].string
        s = str(i.find_all('span', attrs={'class': 'pl'})[0].string)
        # print(re.match('^.*?(\d+).*评价', s, re.S).group(1))
        bookDirt['bookEvaluate'] = re.match('^.*?(\d+).*评价', s, re.S).group(1)
        bookList.append(bookDirt)
        #print(bookDirt)
    return bookList


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

# 存入文本文件
def main(start):
    url = 'https://book.douban.com/top250?start=' + str(start)
    bsObj = get_bs(url)
    print(get_content(bsObj))

    for item in get_content(bsObj):
        print(item)
        write_to_file(item)


# 存入数据库
def main2(start, cursor, db):
    url = 'https://book.douban.com/top250?start=' + str(start)
    bsObj = get_bs(url)
    # print(get_content(bsObj))
    for i, data in enumerate(get_content(bsObj)):
        print(i, data)
        data['bookId'] = i+start
        table = 'doubanbook250'
        keys = ','.join(data.keys())  # id,name,age
        values = ','.join(['%s'] * len(data))  # %s,%s,%s
        sql = "INSERT INTO {table}({keys}) values ({values})".format(table=table, keys=keys, values=values)
        cursor.execute(sql, tuple(data.values()))
        db.commit()
        '''
        try:
            if cursor.execute(sql, tuple(data.values())):  # 第二个参数传入data的键值构造的元组，
                print("Successful")
                db.commit()
        except:
            print("Failed")
            db.rollback()
        '''
    '''
    data = {
        'bookId': 1,
        'bookName': '哈利·波特与阿兹卡班的囚徒',
        'bookAddress': 'https://book.douban.com/subject/1071241/',
        'bookImg': 'https://img3.doubanio.com/view/subject/m/public/s1074376.jpg',
        'bookAuthor': '[英] J. K. 罗琳 / 郑须弥 / 人民文学出版社 / 2000-9 / 26.50元',
        'bookScore': '9.0',
        'bookEvaluate': '102489'
    }
    table = 'doubanbook250'
    keys = ','.join(data.keys())  # id,name,age
    values = ','.join(['%s'] * len(data))  # %s,%s,%s
    print(keys)
    print(values)
    sql = "INSERT INTO {table}({keys}) values ({values})".format(table=table, keys=keys, values=values)
    print(sql)
    try:
        if cursor.execute(sql, tuple(data.values())):   # 第二个参数传入data的键值构造的元组，
            print("Successful")
            db.commit()
    except:
        print("Failed")
        db.rollback()
    db.close()
    '''


if __name__ == "__main__":
    '''
    for i in range(10):
        main(i*25)
    '''
    '''
    # 将数据存入数据库
    db1 = pymysql.connect(host='localhost', user='root', password='wujinxing718', port=3306, database='spiders')
    cursor1 = db1.cursor()
    for i in range(10):
        main2(i*25, cursor1, db1)
    db1.commit()
    db1.close()
    '''
    pass