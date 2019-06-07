import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

'''
request ： 它是最基本的 HTTP 请求模块，可以用来模拟发送请求 。 就像在浏览器里输入网址, 然后回车一样，只需要给库方法传入 URL 以及额外的参数，就可以模拟实现这个过程了 。
error ： 异常处理模块，如果出现请求错误 ， 我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止 。
parse ： 一个工具模块，提供了许多 URL 处理方法，比如拆分、解析 、 合并等 。
robot parser ：主要是用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。
'''

# 发送请求
# 1 urlopen
reponse = urllib.request.urlopen('https://www.python.org')
# print(reponse.read().decode('utf-8'))       # 抓取网页
print(type(reponse))    # <class 'http.client.HTTPResponse'>
print(reponse.status)   # 输出了响应的状态码和响应的头信息
print(reponse.getheaders())     # 响应的头信息
print(reponse.getheader('Server'))      # 调用 getheader()方法并传递一个参数 Server 获取了响应头中的 Server 值，结果是 nginx ，意思是服务器是用 Nginx搭建的 。

#   1. urlopen的data参数  data 参数是可选的 。 如果要添加该参数，并且如果它是字节流编码格式的内容，即 bytes 类型，
# 则需要通过 bytes （）方法转化。 另外，如果传递了这个参数，则它的请求方式就不再是 GET 方式，而
# 是 POST 方式 。
'''
传递了一个参数 word ，值是 hello o 它需要被转码成 bytes(字节流)类型 。 其中转字
节流采用了 bytes()方法，该方法的第一个参数需要是 str (字符串)类型，需要用 urllib.parse 模
块里的 urlencode()方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为 utf8 。'''
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
reponse = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(reponse.read())

# 2 .urllib的timeout参数  设置超时时间，单位为秒，意思就是如果请求超 出 了设置的这个时间， 还没有得到响应 ， 就会抛出异常。
#response = urllib.request .urlopen('http: //httpbin .org/get', timeout=1)
#print(response .read())
'''
通过设置这个超时时间来控制一个网页如果长时间未响应，就跳过它的抓取 。 这可以
利用 try except 语句来实现'''
import socket
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get',  timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# Request
'''
利用 urlopen()方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一
个完整的请求 。 如果请求中需要加入 Headers 等信息，就可以利用更强大的 Request 类来构建。
'''
import urllib.request
request = urllib.request.Request('https://www.baidu.com')
response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))
# 构建多个参数
url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)', 'Host': 'httpbin.org'}
dict = {'name': 'Germey'}
data= bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
#print(response. read(). decode('utf-8'))
#  url 即请求 URL, headers 中指定了 User-Agent 和# Host ，参数 data 用 urlencode()和 bytes()方法转成字节流 。指定了请求方式为 POST

# 代理 做爬虫的时候，免不了要使用代理，如果要添加代理，可以这样做：
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read() .decode('utf-8'))
except URLError as e:
    print(e .reason)
# [WinError 10061] 由于目标计算机积极拒绝，无法连接。

# Cookies
'''
首先 ，我们必须声明一个 CookieJar 对象. 接下来, 就需要利用 HTTPCookieProcessor 来构建一个
Handler, 最后利用 build_opener()方法构建出 Opener, 执行 open()函数即可 。
'''
import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
#for item in cookie:
    #print(item.name + "=" + item.value)

# Robots
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*',  'http://www.jianshu.com/search?q=python&page=1&type=collections'))