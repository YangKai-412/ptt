#爬蟲

import urllib.request as req

import ssl # 在 urllib.error.URLError異常時加入

import bs4


url = 'https://www.ptt.cc/bbs/movie/index.html'
ssl._create_default_https_context = ssl._create_unverified_context
#建立一個 Request 物件, 附加 Request Headers 的資訊
request = req.Request(url, headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    })

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

root = bs4.BeautifulSoup(data, 'html.parser')
titles = root.find_all('div', class_='title') #尋找所有 class_='title' 的 div 標籤

for title in titles:
    if title.a != None: # 如果標題包含 a 標籤 印出來
        print(title.a.string)