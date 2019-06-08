from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import json


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


def main(start):
    url = 'https://book.douban.com/top250?start=' + str(start)
    bsObj = get_bs(url)
    print(get_content(bsObj))

    for item in get_content(bsObj):
        print(item)
        write_to_file(item)


if __name__ == "__main__":
    for i in range(10):
        main(i*25)