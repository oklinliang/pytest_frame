import requests
import time

zentaohost = "http://zentao.tihal.cn:15000"
login_url = zentaohost + '/zentao/user-login.html'
add_bug_url = zentaohost + '/zentao/bug-create-7-0-moduleID=0.html'
test_url = zentaohost + '/zentao/testcase-browse-7--all-0-id_desc.html'


def add_bug(title,steps):
    header = {
        'Content-Type': "application/x-www-form-urlencoded; charset=utf-8"
    }
    data = {
        "account":"linliang",
        "password":"Passw0rd"
    }
    s = requests.session()
    s.post(login_url, headers=header, data=data)

    # bug_data = {
    #     "product": "7",  # int   所属产品 * 必填
    #     "openedBuild": "trunk",  # int | trunk   影响版本 * 必填
    #     "branch": "0",  # int    分支 / 平台
    #     "module": "0",  # int    所属模块
    #     "project": "",  # int   所属项目
    #     "assignedTo": "linliang",  # string 指派给
    #     "deadline": "",  # date 截止日期    日期格式：YY - mm - dd，如：2019 - 01 - 01
    #     "type": "codeerror",
    #     # string   Bug类型   取值范围： | codeerror | interface | config | install | security | performance | standard | automation | designchange | newfeature | designdefect | trackthings | codeimprovement | others
    #     "os": "",
    #     # string 操作系统 取值范围： | all | windows | win8 | win7 | vista | winxp | win2012 | win2008 | win2003 | win2000 | android | ios | wp8 | wp7 | symbian | linux | freebsd | osx | unix | others
    #     "browser": "",
    #     # string    浏览器 取值范围： | all | ie | ie11 | ie10 | ie9 | ie8 | ie7 | ie6 | chrome | firefox | firefox4 | firefox3 | firefox2 | opera | oprea11 | oprea10 | opera9 | safari | maxthon | uc | other
    #     "color": "",  # string  颜色格式：  # RGB，如：#3da7f5
    #     "severity": "3",  # int  严重程度    取值范围：1 | 2 | 3 | 4
    #     "pri": "3",  # int   优先级 取值范围：0 | 1 | 2 | 3 | 4
    #     "mailto": "",  # string 抄送给 填写帐号，多个账号用','分隔。
    #     "keywords": "",  # string   关键词
    #     "title": title,  # string  Bug标题 * 必填
    #     "steps": steps  # string   重现步骤
    # }
    # a = s.post(add_bug_url,headers=header,data=bug_data)
    # print(a.content.decode('utf-8'))
    test_data = {
        "product" : "7"
    }

    a = s.post(test_url,headers=header,data=test_data)
    print(a.content.decode('utf-8'))
    response = s.post(login_url, headers=header, data=data)
    return response.status_code

if __name__ == '__main__':
    add_bug("标题是这个","步骤是这个")

