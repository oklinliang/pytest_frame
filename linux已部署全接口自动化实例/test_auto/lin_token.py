# -*- coding:utf-8 -*-
import json
import lin_config
import requests
import lin_sql_perform

#获取登录token
def login_token(url,headers):
    login_next = "/txearth/login/login"

    login_data = json.dumps({
        "account_no": lin_config.my_user,
        "account_pwd": lin_config.my_pw
    })
    login = requests.request("POST", url + login_next, headers=headers, data=login_data)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))[
        'access_token']
    return log_token

def html_app_getcode(url,headers):
    # getcode_next = "/api/v1.0/user/getCodeTwo"
    # getcode_data = json.dumps({
    #   "common": {
    #     "platform": "android",
    #     "version": "1.0",
    #     "vt": "",
    #     "is_web": 1
    #   },
    #   "req": {
    #     "account_no": lin_config.my_user,
    #     "type": "1"
    #   }
    # })
    # risk_statistics = requests.request("POST", url + getcode_next, headers=headers, data=getcode_data)
    # bb = json.loads(json.dumps(risk_statistics.json()))['code']
    # mycode = bb[0:6]
    mycode = "111111"
    return mycode

def html_app_login_token(url,headers,code):
    # login_next = "/api/v1.0/user/loginApp"
    #
    # login_data = json.dumps({
    #     "common": {
    #         "platform": "android",
    #         "token": "",
    #         "uid": "",
    #         "version": "1.0",
    #         "vt": "",
    #         "is_web": 1
    #     },
    #     "req": {
    #         "pwd": lin_config.my_pw_md5,
    #         "userAccount": lin_config.my_user,
    #         "type": "2",
    #         "code": code
    #     }
    # })
    # login = requests.request("POST", url + login_next, headers=headers, data=login_data)
    # print(login.json())
    # html_app_login_token = json.loads(json.dumps(json.loads(json.dumps(login.json()))['resp']))['access_token']
    # html_app_request_token = json.loads(json.dumps(json.loads(json.dumps(login.json()))['resp']))['token']
    # html_app_request_id = json.loads(json.dumps(json.loads(json.dumps(login.json()))['resp']))['account_id']

    my_dect_a = lin_sql_perform.cmm_account_info_t(lin_config.my_user)
    my_dect_b = lin_sql_perform.select_app_token(lin_config.my_uid)

    html_app_request_id = lin_config.my_uid
    html_app_login_token = my_dect_a['access_token']
    html_app_request_token = my_dect_b['auth_id']
    return html_app_login_token,html_app_request_token,html_app_request_id

