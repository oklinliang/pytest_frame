import requests
import time
import json
import docx
import my_request

def login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "linliang",
        "account_pwd": "QUJDZGVmMTIz"
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))['access_token']
    return log_token

if __name__ == '__main__':
    requ = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    url = "https://crisisresponse.tihal.cn"
    # 设置文档名称为日期
    time_ymd = time.strftime("%Y年%m月%d日")
    time_hms = time.strftime("%H时%M分%S秒")
    # 获取登录用token
    my_token = login_token(requ, url, headers)
    doc = docx.Document()
    my_request.auto_request(url,headers,my_token,doc,time_ymd,time_hms)


