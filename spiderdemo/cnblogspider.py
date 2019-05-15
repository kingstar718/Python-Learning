#conding:utf-8
import requests
import re
import json
from bs4 import BeautifulSoup


r = requests.get('https://www.cnblogs.com/aggsite/UserStats')
print(r.text)


if __name__=="__main__":
    pass