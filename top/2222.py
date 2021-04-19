import requests
import json
import re
import time

requests.packages.urllib3.disable_warnings()

if __name__ == '__main__':
    session = requests.session()
    url = "/connect/authreport?uuid=&uin=MzcxOTA1ODIxNg==&appid=wxe3461d5cb3219371&staytime=0&pageerror=Uncaught%20SyntaxError:%20Invalid%20or%20unexpected%20token||Mozilla/5.0%20(Windows%20NT%2010.0;%20WOW64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/53.0.2785.116%20Safari/537.36%20QBCore/4.0.1320.400%20QQBrowser/9.0.2524.400%20Mozilla/5.0%20(Windows%20NT%206.1;%20WOW64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/53.0.2875.116%20Safari/537.36%20NetType/WIFI%20MicroMessenger/7.0.20.1781(0x6700143B)%20WindowsWechat(0x63010200)"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Mi 10 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045527 Mobile Safari/537.36 MMWEBID/4024 MicroMessenger/8.0.2.1860(0x28000235) Process/tools WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64",
    }
    response = session.get(url, headers=headers)
    print(response)
    print(response.headers)
    headers = requests.head(url).headers
    print(headers)