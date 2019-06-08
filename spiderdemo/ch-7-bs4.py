from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

headers = {
        'Uesr-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
#r = requests.get("https://www.douban.com/review/best/", headers = headers)
#print(r.text)
def demo1():
    html = urlopen("https://www.douban.com/review/best/")
    bsObj = BeautifulSoup(html, features="lxml")
    # print(bsObj.prettify())     # prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出 。
    print(bsObj.title.string)   # 输出HTML中title节点的文本内容
    print(type(bsObj.title))    # <class 'bs4.element.Tag'>
    # 选择因素
    print(bsObj.head)
    print(bsObj.p)
    # 提取信息
    print("bsObj.title.name: "+bsObj.title.name)    # 选取title节点，然后调用name属性就可以得到节点名称：
    # 多个属性获取
    print(bsObj.p.attrs)
    print(bsObj.a.attrs)
    print(bsObj.a.attrs['href'] + " or " + bsObj.a['href'])
    print(bsObj.a.string)       # 利用 string 属性获取节点元素包含的文本内容
    # 再次注意一下，这里选择到的p/a节点是第一个p/a节点,获取的文本也是第一个p/a节点里面的文本

    # 嵌套选择
    print(bsObj.head.title)
    print(bsObj.head.title.string)

    # print(bsObj.p.parents)   # p节点的父节点元素
    # print(list(enumerate(bsObj.a.parents)))
    # 兄弟节点
    # print(list(enumerate(bsObj.a.next_siblings)))


def demo2():
    html = urlopen("https://www.douban.com/review/best/")
    bsObj = BeautifulSoup(html, features="lxml")
    # 方法选择器
    # find_all()
    # print(bsObj.find_all(name='div'))
    # print(bsObj.find_all(attrs={'class': 'main-bd'}))
    # print(bsObj.find_all(name='h2'))
    print(bsObj.select('h2'))
    for i in bsObj.select('h2'):
        print(i.a.string)
        print(i.a['href'])


if __name__ == "__main__":
    # demo1()
    demo2()
    pass