import urllib.request
import json

url = 'https://fanyi.baidu.com/sug'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

data = {
    'kw': 'spider'
}
# post请求的参数，必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, headers=headers,data=data)
response = urllib.request.urlopen(request)
contact = response.read().decode('utf-8')
obj = json.loads(contact)
print(obj)



