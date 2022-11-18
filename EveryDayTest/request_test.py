import requests
import json

import login

requ = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
url = "https://test.tihal.cn:93"

#获取登录用token
my_token = login.login_token(requ,url,headers)
B_and_R_my_token = login.B_and_R_login_token(requ,url,headers)
N_Industrial_my_token = login.N_Industrial_login_token(requ,url,headers)
China_Traffic_my_token = login.China_Traffic_login_token(requ,url,headers)
T_Hrisk_my_token = login.T_Hrisk_login_token(requ,url,headers)

def qyjgzs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":\"1\"}\n"
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + my_token, data=my_data, headers=headers)
    #企业项目总数
    qyjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_total']
    return qyjgzs

def zbjgzs():
    xmgl = "/xearth/project/project-statistics"
    zbjgzs_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    # 总部项目总数
    zbjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(zbjgzs_json.json()))['data']))['record']))['project_total']
    return zbjgzs

def jgzrs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":4,\"id\":\"139\"}"
    jgzrs_json = requests.request("POST", url + xmgl + "?access-token=" + my_token, data=my_data, headers=headers)
    # 企业项目总数
    jgzrs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(jgzrs_json.json()))['data']))['record']))['people_count']
    return jgzrs

def xyqz():
    xmgl = "/xearth/epidemic/total"
    xyqz_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    xyqz = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(xyqz_json.json()))['data']))['record']))[
        'treating_total']
    return xyqz

def ljqz():
    xmgl = "/xearth/epidemic/total"
    ljqz_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    ljqz = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(ljqz_json.json()))['data']))['record']))[
        'confirmed_total']
    return ljqz

def xyzy():
    xmgl = "/xearth/epidemic/total"
    xyzy_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    xyzy = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(xyzy_json.json()))['data']))['record']))[
        'cures_total']
    return xyzy

def xysw():
    xmgl = "/xearth/epidemic/total"
    xysw_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    xysw = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(xysw_json.json()))['data']))['record']))[
        'deaths_total']
    return xysw

def jgrs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":\"4\"}\n"
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + my_token, data=my_data, headers=headers)
    #机构在各大洲的人数
    jgrs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing']
    return jgrs

def other_rs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":4,\"id\":\"207\"}"
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + my_token, data=my_data, headers=headers)
    #其他机构人数校正
    qyjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing_value']
    return qyjgzs

def other_jgzs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":4,\"id\":\"207\"}"
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + my_token, data=my_data, headers=headers)
    #某机构公司下的机构总数
    other_jgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing_value']
    return other_jgzs

def shandong_week_no():
    xmgl = "/xearth/report/weekly-index-v2"
    shandong_week_no_json = requests.request("POST", url + xmgl + "?access-token=" + my_token,headers=headers)
    # 总部项目总数
    shandong_week_no = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(shandong_week_no_json.json()))['data']))['record']))[0]))['phase']
    return shandong_week_no


#一带一路用的接口
def B_and_r_zbjgzs():
    xmgl = "/xearth/project/project-statistics"
    zbjgzs_json = requests.request("POST", url + xmgl + "?access-token=" + B_and_R_my_token,headers=headers)
    # 总部项目总数
    B_and_r_zbjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(zbjgzs_json.json()))['data']))['record']))['project_total']
    return B_and_r_zbjgzs

def B_and_r_week_no():
    xmgl = "/xearth/report/weekly-index-v2"
    B_and_r_week_no_json = requests.request("POST", url + xmgl + "?access-token=" + B_and_R_my_token,headers=headers)
    # 总部项目总数
    B_and_r_week_no = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(B_and_r_week_no_json.json()))['data']))['record']))[0]))['phase']
    return B_and_r_week_no

#北方工业用的接口
def N_Industrial_zbjgzs():
    xmgl = "/xearth/project/project-statistics"
    zbjgzs_json = requests.request("POST", url + xmgl + "?access-token=" + N_Industrial_my_token,headers=headers)
    # 总部项目总数
    N_Industrial_zbjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(zbjgzs_json.json()))['data']))['record']))['project_total']
    return N_Industrial_zbjgzs

def N_Industrial_week_no():
    xmgl = "/xearth/report/weekly-index-v2"
    N_Industrial_week_no_json = requests.request("POST", url + xmgl + "?access-token=" + N_Industrial_my_token,headers=headers)
    # 总部项目总数
    N_Industrial_week_no = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(N_Industrial_week_no_json.json()))['data']))['record']))[0]))['phase']
    return N_Industrial_week_no

#中交集团
def China_Traffic_zbjgzs():
    xmgl = "/xearth/project/project-statistics"
    zbjgzs_json = requests.request("POST", url + xmgl + "?access-token=" + China_Traffic_my_token,headers=headers)
    # 总部项目总数
    China_Traffic_zbjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(zbjgzs_json.json()))['data']))['record']))['project_total']
    return China_Traffic_zbjgzs

def China_Traffic_jgrs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":\"4\"}\n"
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + China_Traffic_my_token, data=my_data, headers=headers)
    #机构在各大洲的人数
    jgrs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing']
    return jgrs

def China_Traffic_other_rs():
    xmgl = "/xearth/project/project-statistics"
    my_data = json.dumps({
        "type_id": "1",
        "id": "2685",
        "is_country": 1,
        "company_id": "1279"
        })
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + China_Traffic_my_token, data=my_data, headers=headers)
    #其他机构人数校正
    qyjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing_value']
    return qyjgzs

def China_Traffic_other_jgzs():
    xmgl = "/xearth/project/project-statistics"
    my_data = json.dumps({
        "type_id": "1",
        "id": "2685",
        "is_country": 1,
        "company_id": "1279"
    })
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + China_Traffic_my_token, data=my_data, headers=headers)
    #某机构公司下的机构总数
    other_jgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing_value']
    return other_jgzs

def China_Traffic_week_no():
    xmgl = "/xearth/report/weekly-index-v2"
    China_Traffic_week_no_json = requests.request("POST", url + xmgl + "?access-token=" + China_Traffic_my_token,headers=headers)
    # 总部项目总数
    China_Traffic_week_no = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(China_Traffic_week_no_json.json()))['data']))['record']))[0]))['phase']
    return China_Traffic_week_no


#鼎昊国际
def T_Hrisk_zbjgzs():
    xmgl = "/xearth/project/project-statistics"
    zbjgzs_json = requests.request("POST", url + xmgl + "?access-token=" + T_Hrisk_my_token,headers=headers)
    # 总部项目总数
    T_Hrisk_zbjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(zbjgzs_json.json()))['data']))['record']))['project_total']
    return T_Hrisk_zbjgzs

def T_Hrisk_jgrs():
    xmgl = "/xearth/project/project-statistics"
    my_data = "{\"type_id\":\"4\"}\n"
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + T_Hrisk_my_token, data=my_data, headers=headers)
    #机构在各大洲的人数
    jgrs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing']
    return jgrs

def T_Hrisk_other_rs():
    xmgl = "/xearth/project/project-statistics"
    my_data = json.dumps({
        "type_id": "1",
        "id": "451"
        })
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + T_Hrisk_my_token, data=my_data, headers=headers)
    #其他机构人数校正
    qyjgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing_value']
    return qyjgzs

def T_Hrisk_other_jgzs():
    xmgl = "/xearth/project/project-statistics"
    my_data = json.dumps({
        "type_id": "1",
        "id": "451"
        })
    qyxmzs_json = requests.request("POST", url + xmgl + "?access-token=" + T_Hrisk_my_token, data=my_data, headers=headers)
    #某机构公司下的机构总数
    other_jgzs = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(qyxmzs_json.json()))['data']))['record']))['project_bing_value']
    return other_jgzs

def T_Hrisk_jgzrs():
    xmgl = "/xearth/plague/project"
    jgzrs_json = requests.request("POST", url + xmgl + "?access-token=" + T_Hrisk_my_token, headers=headers)
    # 企业项目总数
    T_Hrisk_jgzrs = \
    json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(jgzrs_json.json()))['recode']))['count']))[
        'people_count']
    return T_Hrisk_jgzrs

def T_Hrisk_week_no():
    xmgl = "/xearth/report/weekly-index-v2"
    T_Hrisk_week_no_json = requests.request("POST", url + xmgl + "?access-token=" + T_Hrisk_my_token,headers=headers)
    # 总部项目总数
    T_Hrisk_week_no = json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(json.loads(json.dumps(T_Hrisk_week_no_json.json()))['data']))['record']))[0]))['phase']
    return T_Hrisk_week_no

