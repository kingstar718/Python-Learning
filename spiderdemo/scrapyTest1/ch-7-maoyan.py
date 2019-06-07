import requests
import re
import json

# https://maoyan.com/board/4
# https://maoyan.com/board/4?offset=10
# https://maoyan.com/board/4?offset=20

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac 0S X 10_11_4)AppleWebKit/537.36(KHTML, like Gecko)'
                      'Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text

# 首先，需要提取它的排名信息,而它的排名信息是在class为board-index-i节点内，这里利用非贪婪匹配来提取i节点内的信息，正则表达式写为：
# <dd>.*?board-inde.*?>{.*?}</i>
# 随后需要提取电影的图片，可以看到，后面有a节点，其内部有两个img节点。经过检查后发现，第二个img节点的data-src属性是图片的链接。
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
# 再往后,需要提取电影的名称,它在后面的p节点内,class为name.所以,可以用name做一个#标志位,然后进一步提取到其内a节点的正文内容，
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>
# 再提取主演 、 发布时间、评分等内容时，都是同样的原理。 最后，正则表达式写为：
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?
# releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?'
        'data-src="(.*?)".*?'
        'name.*?a.*?>(.*?)</a>.*?'
        'star.*?>(.*?)</p>.*?'
        'releasetime.*?>(.*?)</p>.*?'
        'integer.*?>(.*?)</i>.*?'
        'fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    sumDirt=[]
    for item in items:
        sDirt={}
        '''
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }'''
        sDirt['index'] = item[0]
        sDirt['image'] = item[1]
        sDirt['title'] = item[2].strip()
        sDirt['actor'] = item[3].strip()[3:] if len(item[3]) > 3 else ''
        sDirt['time'] = item[4].strip()[5:] if len(item[4]) > 5 else ''
        sDirt['score'] = item[5].strip() + item[6].strip()
        sumDirt.append(sDirt)
        #print(sDirt)
    #print(sumDirt)
    return sumDirt


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)