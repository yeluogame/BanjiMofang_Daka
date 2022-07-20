import random
import time
import logging
import urllib.request
import urllib.parse
from lxml import etree


def getCookie():
    """
    获取Cookie
    :return: None
    """
    headers = {
        "Host": "k8n.cn",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Cookie": "remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=1390882%7CX3qRyCFG3bj1LK1vUyyNnIjEOYT8v2tiwtfsu6a7nkVS3Hxda6Po2MHhcRJW%7C%242y%2410%24%2F2PV9ExAk7IqWgovBUAHwuEFSqq8Duht%2FxcNejeG7RMQg8.c7ySie; wxid=ollOC0YNuQaCILbMwS7wGTzZgNn0$1657704135$33f47d3de17cbb1e2452655eb15888b3",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/4019 MicroMessenger/8.0.3.1880(0x28000334) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32',
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
    }
    baseurl = 'http://k8n.cn/student'
    request = urllib.request.Request(url=baseurl, headers=headers)
    try:
        response = urllib.request.urlopen(request, timeout=10)
    except Exception as e:
        print("Cookie Fail >>> ", e)
        return
    cookie = response.getheader("Set-Cookie")[:47]
    logging.info("Cookie successfully >>> " + str(cookie))
    old_cookie = headers['Cookie']
    cookie = cookie + ";" + old_cookie
    logging.info("Return Cookie >>> " + str(cookie))
    return cookie


def putData(cookie=None, course=None):
    """
    提交打卡数据
    :param cookie:打卡时必须携带Cookie
    :param course: 对应的班级ID
    :return: None
    """
    if cookie == '' or cookie is None:
        logging.error("Cookie is Null")
        return
    if course == '' or course == 0 or course is None:
        logging.error("Course is Null")
        return
    headers = {
        'Host': 'k8n.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/4019 MicroMessenger/8.0.3.1880(0x28000334) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'com.tencent.mm',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie
    }

    put_url = "http://k8n.cn/student/course/" + str(course) + "/profile/29"
    data = {
        'form_id': 45,
        'formid': 58,
        'formdata[fn_1]': 36.6,
        'formdata[fn_2]': 0,
        'formdata[fn_3]': 0,
        'formdata[fn_4]': 0,
        'formdata[fn_5]': 0,
        # 打卡地址必须遵循该格式，否则无法正常打卡
        'formdata[fn_6]': '江西省,赣州市,于都县|25.952524,115.415089',
        'formdata[gps_addr]': '江西省,赣州市,于都县|25.952524,115.415089',
        'formdata[gps_xy]': '25.952524,115.415089',
        '_score': 0
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=put_url, headers=headers, data=data)
    try:
        response = urllib.request.urlopen(request, timeout=10)
        desc = getDesc(response.read().decode())
        if "班级魔方用户中心" == desc:
            logging.info("打卡成功")
        else:
            logging.warning(desc)
    except Exception as e:
        logging.error(e)


def getDesc(html):
    """
    解析打卡后的回调网页
    :param html: 返回的网页数据
    :return: 返回网页中的提示信息
    """
    tree = etree.HTML(html)
    try:
        desc = tree.xpath('/html/head/title/text()')[0]
        return desc
    except IndexError:
        desc = tree.xpath('/html/body/div[2]/div[2]/text()')[0]
        return desc
    except Exception as e:
        logging.error("Callback Error")
        return e


def index1(cookie):
    """
    模拟用户操作，混淆
    :param cookie:
    :return:
    """
    if cookie == '' or cookie is None:
        logging.error("Cookie is Null")
        return
    headers = {
        'Host': 'k8n.cn',
        'Cookie': cookie,
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G955N BuBuildild/NRD90M.G955NKSU1AQDC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/4019 MicroMessenger/8.0.3.1880(0x28000334) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32',
        'Referer': 'http//k8n.cn/student',
        'Accept-Language': ' zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': ' gzip, deflate'
    }
    url = 'http://k8n.cn/student/course/46772'
    request = urllib.request.Request(url=url, headers=headers)
    try:
        urllib.request.urlopen(request, timeout=10)
        pass
    except Exception as e:
        print(e)


def index2(cookie):
    """
    模拟用户操作，混淆
    :param cookie:
    :return:
    """
    if cookie == '' or cookie is None:
        logging.error("Cookie is Null")
        return
    headers = {
        'Host': 'k8n.cn',
        'Cookie': cookie,
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G955N Build/NRD90M.G955NKSU1AQDC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 MMWEBID/4019 MicroMessenger/8.0.3.1880(0x28000334) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32',
        'Referer': 'http://k8n.cn/student/course/46772',
        'Accept-Language': ' zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': ' gzip, deflate'
    }
    url = 'http://k8n.cn/student/course/46772/covid19/index'
    request = urllib.request.Request(url=url, headers=headers)
    try:
        urllib.request.urlopen(request, timeout=10)
        pass
    except Exception as e:
        print(e)


def main():
    # logging.basicConfig(level=logging.INFO, filename='./daka.log', filemode='a',
    #                     format='%(asctime)s - %(levelname)s :%(message)s')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')
    cookie = getCookie()
    time.sleep(random.randint(1, 3))
    index1(cookie)
    time.sleep(random.randint(1, 3))
    index2(cookie)
    time.sleep(random.randint(1, 3))
    # 班级ID
    course = 45123
    logging.info("Start Work >>> Cookie:" + str(cookie) + ",Course:" + str(course))
    putData(cookie, course)


if __name__ == "__main__":
    main()
    pass
