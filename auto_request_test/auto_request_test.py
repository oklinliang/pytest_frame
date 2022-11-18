
# -*- coding:utf-8 -*-
import yagmail
import requests
import time
import json
#获取登录token
def login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "linliang",
        "account_pwd": "QUJDZGVmMTIz"
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))['access_token']
    return log_token
#邮件发送系统
def auto_mail(a):
    args = {
        "user": "ok.linliang@163.com",  # 发邮件账号
        "password": "1991119",  # 发件账号对应的密码（QQ使用的是授权码，而不是QQ密码）
        "host": "smtp.163.com",  # 邮件账号的SMTP服务器
        "port": "465"  # SMTP服务器端口 465
    }
    emailList = ["jing_910119@163.com","sorocktech@outlook.com"]
    # 收件人列表
    email = yagmail.SMTP(**args)
    email.send(to=emailList, subject=time.strftime('%Y-%m-%d %X',time.localtime()), contents=a)



#接口配置
def auto_request():
    nothing_data = [
        "/xearth/epidemic-daily/list",
        "/xearth/risk-type/click-type",
        "/xearth/project/project-statistics",
        "/xearth/plague/project-v2",
        "/xearth/user/index",
        "/xearth/project-file/get-file-menu",
        "/xearth/statistics/sentiment-tree-v2",
        "/xearth/country/country-v2",
        "/xearth/report/weekly-index-v2",
        "/xearth/statistics/onekey-alarm",
        "/xearth/statistics/receive-police-list-one",
        "/xearth/emergency/process-list"]
    a = len(nothing_data)
    for i in range(a):
        no_data_json = requests.request("POST", url + nothing_data[i] + "?access-token=" + my_token, headers=headers)
        time.sleep(2)
        if(no_data_json.status_code != 200):
            response_time = str(no_data_json.elapsed.total_seconds())
            request_json = str(no_data_json.json())
            request_url = str(no_data_json.url)
            err_list.append("接口名称："+ request_url)
            err_list.append("响应时间：" + response_time)
            err_list.append("接口返回："+ request_json)
        else:
            response_time = str(no_data_json.elapsed.total_seconds())
            request_json = str(no_data_json.json())
            request_url = str(no_data_json.url)
            response_time_float = float(response_time)
            if(response_time_float >= 2):
                err_list.append("接口名称：" + request_url)
                err_list.append("响应时间：" + response_time)
                err_list.append("接口返回：" + request_json)
    have_data = (
        "/xearth/risk-type/get-type",
        "/xearth/area-list-new/get-area-risk-v2"
    )
    have_data_data = [
        '"{\"source\":\"all\"}"',
        '"{\"area_id\":0,\"type_id\":\"17\"}"'
    ]
    b = len(have_data)
    for i in range(b):
        have_data_json = requests.request("POST", url + have_data[i] + "?access-token=" + my_token,data=have_data_data[i],headers=headers)
        time.sleep(2)
        if (no_data_json.status_code != 200):
            response_time = str(no_data_json.elapsed.total_seconds())
            request_json = str(no_data_json.json())
            request_url = str(no_data_json.url)
            err_list.append("接口名称：" + request_url)
            err_list.append("响应时间：" + response_time)
            err_list.append("接口返回：" + request_json)
        else:
            response_time = str(no_data_json.elapsed.total_seconds())
            request_json = str(no_data_json.json())
            request_url = str(no_data_json.url)
            response_time_float = float(response_time)
            if (response_time_float >= 2):
                err_list.append("接口名称：" + request_url)
                err_list.append("响应时间：" + response_time)
                err_list.append("接口返回：" + request_json)


    a = len(err_list)
    type(err_list)
    if(a != 0):
        auto_mail(err_list)

#定时任务
def timer():
    while True:
        auto_request()
        time.sleep(900)


requ = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://crisisresponse.tihal.cn"

#获取登录用token
my_token = login_token(requ,url,headers)

err_list = []
timer()
# auto_request()
