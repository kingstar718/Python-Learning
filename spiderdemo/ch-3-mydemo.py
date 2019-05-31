from urllib.request import urlopen
from bs4 import BeautifulSoup
import _ssl


#ssl._create_default_https_context = ssl._create_unverified_context
html = urlopen("https://www.77kpp.com/vod-type-id-1-pg-1.html")
bsObj = BeautifulSoup(html, features="html5lib")
print(bsObj)