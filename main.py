import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
# 一个类型和6个方法
# response神HttpResponse类型
print(type(response))
# 按一个字节一个字节的去读，
response.read()
# 返回5个字节
response.read(5)
# 读取一行
response.readline()
# 读取所有行
response.readlines()
# 返回状态码
response.getcode()
# 返回URL
response.geturl()
# 返回响应头
response.getheaders()

# 下载方法
# url下载路径，filename文件名字
urllib.request.urlretrieve(url, 'baidu.html')
# 将汉字转为Unicode编码
name = urllib.parse.quote('中文')
print(name)

# urlencode多个参数转化unicode,必须为字典类型
data = {
    'wd': '中国'
}
a = urllib.parse.urlencode(data)
print(a)

