from lxml import etree
import urllib.request

headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
request = urllib.request.Request(url="http://www.baidu.com",headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode()
tree = etree.HTML(content)
result = tree.xpath('//*[@id="sua"]/@value')[0]
print(result)