import requests
import lin_sql_perform
"""
    配置项都在这里

"""

#获取token参数
request_requ = requests.session()
request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    'Content-Type': 'application/json',
    'Connection': 'close'
}
request_url = "https://dev.tihal.cn:88"



#禅道的配置文件
zentaohost = "http://zentao.tihal.cn:15000"
login_url = zentaohost + '/zentao/user-login.html'
add_bug_url = zentaohost + '/zentao/bug-create-7-0-moduleID=0.html'

#mysql配置文件
host = '192.168.120.231'
port = 3306
db = 'earth_2021819'
user = 'root'
password = 'earth'

#帐号密码
my_user = '13671174909'
my_pw = 'MTJRV2FzenhA'
my_pw_md5 = 'dc5371cacbd433cfb31ac5d826589e4b'
my_dect = lin_sql_perform.cmm_account_info_t(my_user)
my_uid = my_dect['account_id']