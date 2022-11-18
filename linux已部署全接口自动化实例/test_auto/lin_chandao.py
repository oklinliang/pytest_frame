import requests
import lin_config

"""
    禅道在这里调用

"""



def add_bug(title,steps):
    header = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    data = {
        "account":"linliang",
        "password":"Passw0rd"
    }
    s = requests.session()
    s.post(lin_config.login_url, headers=header, data=data)


    bug_header = {
        'Content-Type': "application/x-www-form-urlencoded; charset=utf-8"
    }
    bug_data = {
        "product": "7",  # int   所属产品 * 必填
        "openedBuild": "trunk",  # int | trunk   影响版本 * 必填
        "branch": "0",  # int    分支 / 平台
        "module": "0",  # int    所属模块
        "project": "",  # int   所属项目
        "assignedTo": "fanbaohong",  # string 指派给
        "deadline": "",  # date 截止日期    日期格式：YY - mm - dd，如：2019 - 01 - 01
        "type": "codeerror",
        # string   Bug类型   取值范围： | codeerror | interface | config | install | security | performance | standard | automation | designchange | newfeature | designdefect | trackthings | codeimprovement | others
        "os": "",
        # string 操作系统 取值范围： | all | windows | win8 | win7 | vista | winxp | win2012 | win2008 | win2003 | win2000 | android | ios | wp8 | wp7 | symbian | linux | freebsd | osx | unix | others
        "browser": "",
        # string    浏览器 取值范围： | all | ie | ie11 | ie10 | ie9 | ie8 | ie7 | ie6 | chrome | firefox | firefox4 | firefox3 | firefox2 | opera | oprea11 | oprea10 | opera9 | safari | maxthon | uc | other
        "color": "",  # string  颜色格式：  # RGB，如：#3da7f5
        "severity": "3",  # int  严重程度    取值范围：1 | 2 | 3 | 4
        "pri": "3",  # int   优先级 取值范围：0 | 1 | 2 | 3 | 4
        "mailto": "",  # string 抄送给 填写帐号，多个账号用','分隔。
        "keywords": "",  # string   关键词
        "title": title,  # string  Bug标题 * 必填
        "steps": steps  # string   重现步骤
    }
    a = s.post(lin_config.add_bug_url,headers=bug_header,data=bug_data)
    # print(a.content.decode('utf-8'))
    response = s.post(lin_config.login_url, headers=header, data=data)
    return response.status_code
