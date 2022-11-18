import time
import json
import unittest
import driver


dr = driver.dr
dr.set_window_size(1920,1080)
class 登录(unittest.TestCase):
    def 山东高速登录(self):
        dr.find_element_by_id("normal_login_account_no").send_keys("linliang")
        dr.find_element_by_id("normal_login_account_pwd").send_keys("ABCdef123")
        captcha = input("验证码")
        dr.find_element_by_id("normal_login_captcha").send_keys(captcha)
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        # 暂停20秒等待页面相应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("登录失败")

    def 一带一路登录(self):
        dr.find_element_by_id("normal_login_account_no").send_keys("llyidaiyilu")
        dr.find_element_by_id("normal_login_account_pwd").send_keys("Passw0rd")
        captcha = input("验证码")
        dr.find_element_by_id("normal_login_captcha").send_keys(captcha)
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        # 暂停20秒等待页面相应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "港口信息"):
            pass
        else:
            raise EnvironmentError("登录失败")

    def 北方工业登录(self):
        dr.find_element_by_id("normal_login_account_no").send_keys("llbeifanggongye")
        dr.find_element_by_id("normal_login_account_pwd").send_keys("Passw0rd")
        captcha = input("验证码")
        dr.find_element_by_id("normal_login_captcha").send_keys(captcha)
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        # 暂停20秒等待页面相应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("登录失败")

    def 中交集团登录(self):
        dr.find_element_by_id("normal_login_account_no").send_keys("llzhongjiaojituan")
        dr.find_element_by_id("normal_login_account_pwd").send_keys("Passw0rd")
        captcha = input("验证码")
        dr.find_element_by_id("normal_login_captcha").send_keys(captcha)
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        # 暂停20秒等待页面相应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("登录失败")


    def 鼎昊国际登录(self):
        dr.find_element_by_id("normal_login_account_no").send_keys("bb")
        dr.find_element_by_id("normal_login_account_pwd").send_keys("ABCdef123")
        captcha = input("验证码")
        dr.find_element_by_id("normal_login_captcha").send_keys(captcha)
        time.sleep(1)
        dr.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        # 暂停20秒等待页面相应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("登录失败")


def login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "linliang",
        "account_pwd": "QUJDZGVmMTIz"
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))[
        'access_token']
    return log_token

def B_and_R_login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "llyidaiyilu",
        "account_pwd": "UGFzc3cwcmQ="
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))[
        'access_token']
    return log_token

def N_Industrial_login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "llbeifanggongye",
        "account_pwd": "UGFzc3cwcmQ="
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))[
        'access_token']
    return log_token

def China_Traffic_login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "llzhongjiaojituan",
        "account_pwd": "UGFzc3cwcmQ="
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))[
        'access_token']
    return log_token

def T_Hrisk_login_token(requ,url,headers):
    login_next = "/xearth/login/login"

    login_date = {
        "account_no": "bb",
        "account_pwd": "QUJDZGVmMTIz"
    }

    login = requ.post(url + login_next, data=login_date, headers=headers)
    log_token = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(login.json()))['data']))['record']))[
        'access_token']
    return log_token