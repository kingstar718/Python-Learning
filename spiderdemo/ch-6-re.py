import re


'''
正则表达式
'''


def demo1():
    # match()法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；如果不匹配，就返回None
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    '''
    以Hello开头；
    然后\s匹配空向字符，用来匹配目标字符串的空格；
    \d匹配数字，3个\d匹配123；
    然后再写1个\s匹配空格；
    后面还有4567，我们其实可以依然用4个\d来匹配，但是这么写比较烦琐，所以后面可以跟{4}以代表匹配前面的规则4次，也就是匹配4个数字；
    然后后面再紧接l个空白字符，
    最后\w{10}匹配10个字母及下划线。
    我们注意到，这里其实并没有把目标字符串匹配完，不过这样依然可以进行匹配，只不过匹配结果短一点而已。'''
    # ，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)   # <re.Match object; span=(0, 25), match='Hello 123 4567 World_This'>
    print(result.group())   # 输出匹配到的内容 Hello 123 4567 World_This
    print(result.span())    # 匹配范围  (0, 25)


def demo2():
    # 匹配目标
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('Hello\s(\d+)\sWorld', content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())


def demo3():
    # 通用匹配
    """
    .(点)可以匹配任意字符(除换行符)
    *(星)代表匹配前面的字符无限次
    $ 匹配一行字符串的结尾
    :return:
    """
    content = 'Hello 1234567 World_This is a Regex Demo'
    result = re.match('^Hello.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())

    # 贪婪匹配下，.*会匹配尽可能多的字符。
    result = re.match('^He.*(\d+).*Demo$', content)
    result2 = re.match('^He.*?(\d+).*Demo$', content)   # 非贪婪匹配就好了. 非贪婪匹配的写法是.*?，多了一个?
    print(result)
    print(result.group(1))  # 7 尽可能匹配多的字符，这里就把 123456 匹配了
    print(result2)
    print(result2.group(1))     # 1234567


def demo4():
    # 修饰符
    content = '''Hello 1234567 World_This
     is a Regex Demo'''

    result = re.match('^He.*?(\d+).*?Demo$', content)
    result2 = re.match('^He.*?(\d+).*?Demo$', content, re.S)    # 修饰符的作用是使 .匹配包括换行符在内的所有字符
    # print(result.group(1))    # .匹配的是除换行符之外的任意字符
    print(result2.group(1))     # re.S在网页匹配中经常用到.因为HTML节点经常会有换行,加上它,就可以匹配节点与节点之间的换行了

'''
search()，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
也就是说，正则表达式可以是字符串的一部分，在匹配时，search()方法会依次扫描字符串，
直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None。'''
def demo5():
    content = 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings'
    result = re.match('Hello.*?(\d+).*?Demo', content)
    result2 = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)
    print(result2)


'''
search()方法的用法，它可以返回匹配正则表达式的第一个内容，
但是如果想要获取匹配正则表达式的所有内容，那该怎么办呢？这时就要借助 
findall()方法了, 该方法会搜索整个字符串，然后返回匹配正则表达式的所有内容 。'''


# sub
def demo6():
    content = '54aKS4yrsoiRS4ixSL2g'
    # 第一个参数传入＼ d＋来匹配所有的数字，第二个参数为替换成的字符串（如果去掉
    # 该参数的话，可以赋值为空），第三个参数是原字符串 。
    content = re.sub('\d+', '', content)
    print(content)


def demo7():
    content1 = '2016-12-15 12:00'
    content2 = '2016-12-17 12:55'
    content3 = '2016-12-22 13:21'
    pattern = re.compile('\d{2}:\d{2}')     # 借助compile()法将正则表达式编译成一个正则表达式对象，以便复用
    result1 = re.sub(pattern, '', content1)
    result2 = re.sub(pattern, '', content2)
    result3 = re.sub(pattern, '', content3)
    print(result1, result2, result3)


if __name__ == "__main__":
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    demo7()
    pass