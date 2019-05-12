import urllib.request
import ssl
import requests

headers = {
        'Uesr-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
r = requests.get("https://www.douban.com/review/best/", headers = headers)
print(r.text)