import requests
import re

# r = requests.get('https://www.baidu.com')
# print(type(r))  # <class 'requests.models.Response'>
# print(r.status_code)    # 200
# print(type(r.text))     # <class 'str'>
# print(r.text)
# print(r.cookies)    # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

# r = requests.get('http://httpbin.org/get')
# print(r.text)
# 构造参数
# r = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(r.text)
'''
data = {
    'name': 'germey',
    'age': 22
}  # 参数设置params'''
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)
# print(r.json())
# print(type(r.json()))   # JSON 格式的字符串转化为字典。


# 抓知乎页面
def demo1():
    # 加入了 headers信息,其中包含了User-Agent字段信息,也就是浏览器标识信息.如果不加这个,知乎会禁止抓取。
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh; Intel Mac 0S X 10_11_4)AppleWebKit/537.36(KHTML, like Gecko)'
                     'Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)


# 抓二进制数据
def demo2():
    r = requests.get('https://github.com//favicon.ico')
    print(r.text)
    print(r.content)
    # 保存图标
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


def demo3():
    # 不加headers， 不能正常请求
    r = requests.get('https://www.zhihu.com/explore')
    print(r.text)
    # 加入headers
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac 0S X 10_11_4)AppleWebKit/537.36(KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com/explore', headers = headers)
    print(r.text)


def demo4():
    # POST请求
    data = {'name': 'germey', 'age': '22'}
    r = requests.post('http://httpbin.org/post', data=data)
    print(r.text)
    # 响应
    r = requests.get('http://www.jianshu.com')
    print(type(r.status_code), r.status_code)
    print(type(r.headers), r.headers)
    print(type(r.cookies), r.cookies)
    print(type(r.url), r.url)
    print(type(r.history), r.history)


def demo5():
    # 1.文件上传
    files = {'file': open('favicon.ico', 'rb')}
    r = requests.post('http://httpbin.org/post', files=files)
    print(r.text)
    # 2. Cookies
    r = requests.get('http://www.baidu.com')
    print(r.cookies)
    for key,value in r.cookies.items():
        print(key + ' = ' + value)
    # 3.会话维持
    # 获取不到会话
    requests.get('http://httpbin.org/cookies/set/number/123456789')
    r = requests.get('http://httpbin.org/cookies')
    print(r.text)
    # 获取Session利用Session，可以做到模拟同一个会话而不用担心Cookies的问题。它通常用于模拟登录成功之后再进行下一步的操作
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


def demo6():
    response = requests.get('https://www.12306.cn')
    print(response.status_code)


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    demo6()
    pass