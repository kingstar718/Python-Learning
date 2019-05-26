from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="html5lib")

"""
通过 BeautifulSoup 对象，我们可以用 findAll 函数抽取只包含在 <span class="green"></
span> 标签里的文字，这样就会得到一个人物名称的 Python 列表（findAll 是一个非常灵
活的函数，我们后面会经常用到它）：
"""

#f  indAll(tag, attributes, recursive, text, limit, keywords)
#   find(tag, attributes, recursive, text, keywords)

#  bsObj.findAll(tagName, tagAttributes) 可以获取页面中所有指定的标签
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
"""
.get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回
一个只包含文字的字符串。 假如你正在处理一个包含许多超链接、段落和标
签的大段源代码， 那么 .get_text() 会把这些超链接、段落和标签都清除掉，
只剩下一串不带标签的文字。
用 BeautifulSoup 对象查找你想要的信息，比直接在 HTML 文本里查找信
息要简单得多。 通常在你准备打印、存储和操作数据时，应该最后才使
用 .get_text()。一般情况下，你应该尽可能地保留 HTML 文档的标签结构。"""