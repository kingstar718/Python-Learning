#encoding:utf-8
import urllib.request
import urllib.parse

#  urlparse  将urlstr解析成各个组件
url = "http://www.baidu.com"
parsed = urllib.parse.urlparse(url)
print(parsed)

# urljoin（baseurl,newurl,allowFrag=None） 将url的根域名和新url拼合成一个完整的url
new_path = urllib.parse.urljoin(url, "index.html")
print(new_path)

'''
urlopen(url,data,timeout)　　打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作
read() , readline() , readlines() , fileno() , close() 
info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息。
getcode()：返回Http状态码，如果是http请求，200表示请求成功完成;404表示网址未找到。
geturl()：返回请求的url。'''
req = urllib.request.urlopen(url)
print(req.read())

# urlretrieve(url,filename,reporthook,data) 　下载url定位到的html文件,不写路径filename则会被存为临时文件可以用 urllib.urlcleanup() 来清理缓存
#file_name = urllib.request.urlretrieve(url, '%s /b aidu.html' % BASE_DIR)

# urlencode() 　　将dict中的键值对以连接符&划分
dic  = {'name': 'melon', 'age': 18}
data = urllib.parse.urlencode(dic)
print(data)

# GET请求
dic = {'s?wd': "python"}
data = urllib.parse.urlencode(dic)
req = urllib.request.urlopen('http://www.baidu.com/%s'%data)
content = req.read()
print(content)

# POST请求
'''
import json
dic = {'name':'melon','age':18}
data = urllib.parse.urlencode(dic)

req = urllib.request.Request('http://127.0.0.1:8000/index', data.encode())
opener = urllib.request.urlopen(req)
content = json.loads(opener.read().decode())
'''
#当你 urllib.urlopen一个 https 的时候会验证一次 SSL 证书，当目标使用的是自签名的证书时就会出现一个URLError，如果是这样可以在开头加上
import ssl
ssl._create_default_https_context = ssl._create_unverified_context