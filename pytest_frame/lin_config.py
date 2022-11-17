import requests
"""
    配置项都在这里

"""

#获取token参数
request_requ = requests.session()
request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
request_url = "https://crisisresponse.tihal.cn"



#禅道的配置文件
zentaohost = "http://zentao.tihal.cn:15000"
login_url = zentaohost + '/zentao/user-login.html'
add_bug_url = zentaohost + '/zentao/bug-create-7-0-moduleID=0.html'

#mysql配置文件
host = '192.168.1.65'
port = 33060
db = 'tybtest'
user = 'root'
password = 'root'