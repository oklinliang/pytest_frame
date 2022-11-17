# -*- coding:utf-8 -*-
import json
import lin_config

#获取登录token
def login_token():
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "linliang",
        "account_pwd": "QUJDZGVmMTIz"
    }

    login = lin_config.request_requ.post(lin_config.request_url + login_next, data=login_date, headers=lin_config.request_headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))['access_token']
    return log_token