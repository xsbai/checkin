import requests,sys
from util import timer

@timer.timer('01:00:10') #9:00:10
def check_in(COOKIE):
    url = "http://39.96.69.63/phone/yuyue?id=31&states=2"
    payload = 'id=31&states=2'

    headers = {
    'Host': '39.96.69.63',
    'Content-Length': '14',
    'Origin': 'http://39.96.69.63',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/XK_Gemiui_1.3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Crosswalk/22.52.561.4 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://39.96.69.63/phone/signup',
    'Cookie': COOKIE
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    return response.text.encode('utf8')

if __name__ == "__main__":
    COOKIE = sys.argv[1]
    try:
        response = check_in(COOKIE)
        print(response)
    except Exception as e:
        print('运行出错，原因：%s' % e)