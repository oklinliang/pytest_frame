# -*- coding:utf-8 -*-
import yagmail
import requests
import time
import json
import re
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
        "host": "smtpdm.aliyun.com",  # 邮件账号的SMTP服务器
        "port": "465"  # SMTP服务器端口 465
    }
    emailList = ["jing_910119@163.com","sorocktech@outlook.com"]
    # 收件人列表
    email = yagmail.SMTP(**args)
    email.send(to=emailList, subject=time.strftime('%Y-%m-%d %X',time.localtime()), contents=a)



#接口配置
def country_list():
    xmgl = "/xearth/plague/daily"
    country_list_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    # 总部项目总数
    country_list = json.loads(json.dumps(country_list_json.json()))['data']
    return country_list

def FTKs():
    run = ['孟加拉','伊拉克','以色列','巴基斯坦','沙特阿拉伯','新加坡','阿拉伯联合酋长国','越南','中国香港','东帝汶','哈萨克斯坦','阿尔及利亚','安哥拉','中非','乍得','赤道几内亚','加纳','莫桑比克','尼日尔','肯尼亚','苏丹','乌干达','南苏丹','刚果（金）','玻利维亚','厄瓜多尔','塞尔维亚','波斯尼亚 黑塞哥维那（波黑）','俄罗斯','埃塞俄比亚','日本','德国','贝宁','马拉维共和国','哥伦比亚']
    test = str(country_list())
    pattern = re.compile(r"'country_name': '(.*?)', 'land_name'")
    result = pattern.findall(test)
    bb = len(result)
    a = 0
    for i in range(bb):
        if(result[i] == "哥伦比亚"):
            a = i
    b = result[0:a+1]
    c = len(run) - len(b)
    aa = 0
    d = len(b)
    for k in range(c):
        for i in range(d):
            if(b[i] != run[i]):
                run.remove(run[i])
                break
    for i in range(d):
        if(b[i] == run[i]):
            aa = aa+1
    if(aa != d):
        auto_mail("排序错误")
    else:
        auto_mail("排序没有问题")



requ = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://crisisresponse.tihal.cn"

#获取登录用token
my_token = login_token(requ,url,headers)

err_list = []
FTKs()
