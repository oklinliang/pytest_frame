import lin_config
import lin_chandao
import json
import requests
import lin_token
import urllib3

"""
    指挥中心自动化程序
"""
url = lin_config.request_url
headers = lin_config.request_headers
my_token = lin_token.login_token(url, headers)


class Test_指挥中心_舆情预警():
    def test_舆情预警_获取风险预警_种类统计(self):
        url_rq = "/txearth/risk/risk-statistics"
        data = json.dumps({"type_id": "-1", "id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("舆情预警_获取风险预警-种类统计", "接口异常")

    def test_舆情预警_舆情列表(self):
        url_rq = "/txearth/statistics/public-opinion-report"
        data = json.dumps({"begin_date": "2020-01-23", "end_date": "2021-11-26", "country_name": "刚果", "area_id": 2})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("舆情预警_舆情列表", "接口异常")

    def test_舆情预警_预警信息列表(self):
        url_rq = "/txearth/statistics/early-warning-information"
        data = json.dumps(
            {"type_id": "12", "begin_date": "2020-11-23", "end_date": "2022-11-26", "country_name": "刚果", "area_id": 2})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("舆情预警_预警信息列表", "接口异常")

    def test_舆情预警_风险预警_等级列表(self):
        url_rq = "/txearth/risk/get-all-by-country-new"
        data = json.dumps(
            {"id": "1", "type_id": "2", "type": "1", "begin_date": "2021-08-15", "end_date": "2022-08-17"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("舆情预警_风险预警_等级列表", "接口异常")

    def test_舆情预警_安全周报(self):
        url_rq = "/txearth/report/weekly-index"
        data = json.dumps({"pid": 0, "phase": "244"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("舆情预警_安全周报", "接口异常")

    def test_应急指挥_周边资源(self):
        url_rq = "/txearth/coordinates/near-resources"
        data = json.dumps({"lng": "116.4680019", "lat": "39.9545981", "radius": 5000, "type": "2"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_周边资源", "接口异常")

    def test_应急指挥_获取国家_项目下拉框(self):
        url_rq = "/txearth/statistics/get-country-project"
        data = json.dumps({"country_id": 3})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_获取国家_项目下拉框", "接口异常")

    def test_法律法规_新法律法规接口(self):
        url_rq = "/txearth/law/new-law-tree"
        data = json.dumps({"area_id": "1", "file_id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("法律法规_新法律法规接口", "接口异常")

    def test_项目信息_获取区域alpha3(self):
        url_rq = "/txearth/area-list-new/get-alpha3-code"
        data = json.dumps({"area_id": 110})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目信息_获取区域alpha3", "接口异常")

    def test_项目信息_左侧树搜索(self):
        url_rq = "/txearth/area-list-new/search-area"
        data = json.dumps({"name": "东"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目信息_左侧树搜索", "接口异常")

    def test_项目信息_员工数_项目数统计(self):
        url_rq = "/txearth/test/new-tree"
        data = json.dumps({"id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目信息_员工数_项目数统计", "接口异常")

    def test_项目信息_左侧树(self):
        url_rq = "/txearth/area-list-new/area-list-new"
        data = json.dumps({"pid": 1, "type": 0})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目信息_左侧树", "接口异常")

    def test_项目信息_安保信息(self):
        url_rq = "/txearth/project/get-security"
        data = json.dumps({"id": 1, "page": 1, "size": 20})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目信息_安保信息", "接口异常")

    def test_地球_预警分布_v2(self):
        url_rq = "/txearth/risk/get-all-by-country-v2"
        data = json.dumps({"id": "2", "begin_date": "", "end_date": "", "type_id": ""})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_预警分布_v2", "接口异常")

    def test_地球_预警等级(self):
        url_rq = "/txearth/risk/get-all-by-lev"
        data = json.dumps({"id": "1", "begin_date": "", "end_date": "", "type_id": "-1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_预警等级", "接口异常")

    def test_地球_着色(self):
        url_rq = "/txearth/kml/get-area-risk"
        data = json.dumps({"area_id": 98, "type": "dolore dolor culpa"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_着色", "接口异常")

    def test_地球_预警类别(self):
        url_rq = "/txearth/risk/get-all-by-country"
        data = json.dumps({"id": "1", "begin_date": "", "end_date": "", "type_id": "-1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_预警类别", "接口异常")

    def test_地球_根据国家code获取国别信息(self):
        url_rq = "/txearth/country/get-country-info"
        data = json.dumps({"code": "UGA"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_根据国家code获取国别信息", "接口异常")

    def test_地球_获取国家边界线(self):
        url_rq = "/txearth/country/get-boundary"
        data = json.dumps({"id": 110})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_获取国家边界线", "接口异常")

    def test_地球_项目点(self):
        url_rq = "/txearth/kml/all"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("地球_项目点", "接口异常")

    def test_疫情管理_项目_投资_机构列表(self):
        url_rq = "/txearth/epidemic-people/get-project-info"
        data = json.dumps({"id": "2", "type": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_项目_投资_机构列表", "接口异常")

    def test_疫情管理_获取未更新的项目列表(self):
        url_rq = "/txearth/epidemic/get-no-up-project"
        data = json.dumps({"alpha_3": ["KEN", "BDI", "UGA"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_获取未更新的项目列表", "接口异常")

    def test_疫情管理_人员统计(self):
        url_rq = "/txearth/epidemic/get-people-statistics"
        data = json.dumps({"alpha_3": ["KEN", "BDI", "UGA"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_人员统计", "接口异常")

    def test_疫情管理_境外防疫物资动态(self):
        url_rq = "/txearth/epidemic/get-project-drugs-statistics"
        data = json.dumps({"type": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_境外防疫物资动态", "接口异常")

    def test_疫情管理_项目_投资_机构统计信息(self):
        url_rq = "/txearth/epidemic/get-project-statistics"
        data = json.dumps({"alpha_3": "RUS"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_项目_投资_机构统计信息", "接口异常")

    def test_疫情管理_中间统计数(self):
        url_rq = "/txearth/epidemic/map-detail"
        data = json.dumps({"name": "俄罗斯", "country": "俄罗斯", "id": "2047", "alpha_3": ["RUS", "AUS"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_中间统计数", "接口异常")

    def test_疫情管理_获取药品未满足的项目(self):
        url_rq = "/txearth/epidemic/project-drugs"
        data = json.dumps({"alpha_3": "RUS"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_获取药品未满足的项目", "接口异常")

    def test_疫情管理_项目_投资_机构统计信息更多(self):
        url_rq = "/txearth/epidemic/get-project-statistics-more"
        data = json.dumps({"type": "string"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_项目_投资_机构统计信息更多", "接口异常")

    def test_疫情管理_境外防疫物资动更多(self):
        url_rq = "/txearth/epidemic/get-project-drugs-statistics-more"
        data = json.dumps({"type": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_境外防疫物资动更多", "接口异常")

    def test_疫情管理_全球疫情趋势图(self):
        url_rq = "/txearth/epidemic/project-date"
        data = json.dumps({"type": "1", "name": "拉还度", "alpha_3": ["KEN", "BDI", "UGA"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_全球疫情趋势图", "接口异常")

    def test_疫情管理_获取区域国家(self):
        url_rq = "/txearth/epidemic/get-area-country"
        data = json.dumps({"code": "AS"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_获取区域国家", "接口异常")

    def test_疫情管理_人员统计信息更多(self):
        url_rq = "/txearth/epidemic/get-people-statistics-more"
        data = json.dumps({"type": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_人员统计信息更多", "接口异常")

    def test_疫情管理_新闻列表(self):
        url_rq = "/txearth/epidemic/new-news"
        data = json.dumps({"alpha_3": ["KEN", "BDI", "UGA"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_新闻列表", "接口异常")

    def test_疫情管理_全球疫情数据(self):
        url_rq = "/txearth/epidemic/project-all"
        data = json.dumps({"area_code": "AS", "country_code": ["KEN", "BDI", "UGA"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_全球疫情数据", "接口异常")

    def test_疫情管理_境外防疫物资动态_拆分柱状图(self):
        url_rq = "/txearth/epidemic/get-project-drugs-statistics-v2"
        data = json.dumps({"type": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_境外防疫物资动态_拆分柱状图", "接口异常")

    def test_疫情管理_新闻详情(self):
        url_rq = "/txearth/epidemic/news-detail"
        data = json.dumps({"id": 83875})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_新闻详情", "接口异常")

    def test_疫情管理_确诊_累计_疫苗接种分布(self):
        url_rq = "/txearth/epidemic/all-map"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_确诊_累计_疫苗接种分布", "接口异常")

    def test_疫情管理_获取区域总部列表(self):
        url_rq = "/txearth/epidemic-people/get-area"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_获取区域总部列表", "接口异常")

    def test_疫情管理_地图获取区域点(self):
        url_rq = "/txearth/epidemic/regional-point"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_地图获取区域点", "接口异常")

    def test_疫情管理_全球疫情动态(self):
        url_rq = "/txearth/epidemic/total"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("疫情管理_全球疫情动态", "接口异常")

    def test_预案管理_新_预案管理(self):
        url_rq = "/txearth/emergency-plan/new-emergency-plan-file-tree"
        data = json.dumps({"file_id": "1", "area_id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("预案管理_新_预案管理", "接口异常")

    def test_国别风险_国别信息列表(self):
        url_rq = "/txearth/report/country-index"
        data = json.dumps({"country_id": 8, "pid": 2})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("国别风险_国别信息列表", "接口异常")

    def test_国别风险_预警着色(self):
        url_rq = "/txearth/country/get-risk-lev-v2"
        data = json.dumps({"type_id": 1, "pid": 0})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("国别风险_预警着色", "接口异常")

    def test_国别风险_区域下拉框(self):
        url_rq = "/txearth/country/get-area-select"
        data = json.dumps({"pid": 2})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("国别风险_区域下拉框", "接口异常")

    def test_国别风险_列表(self):
        url_rq = "/txearth/country/get-risk-lev"
        data = json.dumps({"type_id": 17, "pid": 1})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("国别风险_列表", "接口异常")

    def test_国别风险_国别风险类型v2(self):
        url_rq = "/txearth/country/get-risk-type-v2"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("国别风险_国别风险类型v2", "接口异常")

    def test_应急资源_应急装备(self):
        url_rq = "/txearth/emergency-drill-resources/emergency-equipment"
        data = json.dumps({"id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急资源_应急装备", "接口异常")

    def test_应急资源_新_应急组织(self):
        url_rq = "/txearth/emergency-resources/emergency-organization"
        data = json.dumps({"id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急资源_新_应急组织", "接口异常")

    def test_应急资源_应急物资(self):
        url_rq = "/txearth/emergency-drill-resources/emergency-supplies"
        data = json.dumps({"id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急资源_应急物资", "接口异常")

    def test_应急资源_应急组织(self):
        url_rq = "/txearth/emergency-resources/emergency-organization"
        data = json.dumps({"id": "110"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急资源_应急组织", "接口异常")

    def test_位置共享_获取单个用户轨迹(self):
        url_rq = "/txearth/interact/user-location"
        data = json.dumps({"user_id": 2994, "map_id": 1})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("位置共享_获取单个用户轨迹", "接口异常")

    def test_位置共享_组织结构列表(self):
        url_rq = "/txearth/desktop-drill/get-i-m-contacts1"
        data = json.dumps({"org_id": "160"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("位置共享_组织结构列表", "接口异常")

    def test_位置共享_获取轨迹(self):
        url_rq = "/txearth/interact/map-interact-start"
        data = json.dumps({"id": "773", "locationX": "116.11212", "locationY": "39.12121"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("位置共享_获取轨迹", "接口异常")

    def test_位置共享_位置共享中途加人(self):
        url_rq = "/txearth/interact/map-middle"
        data = json.dumps({"map_id": 568, "user_id": [3, 4]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("位置共享_位置共享中途加人", "接口异常")

    def test_位置共享_创建位置共享(self):
        url_rq = "/txearth/interact/map-interact-add"
        data = json.dumps({"police_id": 546, "type": 1})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("位置共享_创建位置共享", "接口异常")

    def test_位置共享_位置共享结束(self):
        url_rq = "/txearth/interact/end-map"
        data = json.dumps({"receive_police_id": 546, "type": 1, "map_id": 1})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("位置共享_位置共享结束", "接口异常")

    def test_应急演练_演练结束(self):
        url_rq = "/txearth/desktop-drill/drill-end"
        data = json.dumps({"drill_id": "27"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_演练结束", "接口异常")

    def test_应急演练_开始获取详情(self):
        url_rq = "/txearth/desktop-drill/detail"
        data = json.dumps({"drill_id": "27"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_开始获取详情", "接口异常")

    def test_应急演练_获取统计柱状图(self):
        url_rq = "/txearth/desktop-drill/topic-stat"
        data = json.dumps({"scenario_list_id": "383"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_获取统计柱状图", "接口异常")

    def test_应急演练_演练方案记录详情(self):
        url_rq = "/txearth/desktop-drill/record-detail"
        data = json.dumps({"drill_id": "27"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_演练方案记录详情", "接口异常")

    def test_应急演练_开始与结束列表(self):
        url_rq = "/txearth/desktop-drill/index"
        data = json.dumps({"is_finish": 1})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_开始与结束列表", "接口异常")

    def test_应急演练_演练记录评估方案保存(self):
        url_rq = "/txearth/desktop-drill/evaluation-create"
        data = json.dumps({
            "drill_id": "27",
            "record": [
                {
                    "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir2021111915/1637307076.pdf",
                    "file_name": "安哥拉 国别信息"
                }
            ],
            "evaluation": {
                "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir2021111915/1637306781.pdf",
                "file_name": "安哥拉 国别信息"
            },
            "_csrf": "9hZV8CyiCMCJ9z9zqyRWw89uhrcflfV9J2EyKsKFOdTAIhiHFc5-mbiFej7cRwSkqgG23HWhgSVOGGVGktZcuQ=="
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_演练记录评估方案保存", "接口异常")

    def test_应急演练_演练开始(self):
        url_rq = "/txearth/desktop-drill/drill-start"
        data = json.dumps({"drill_id": "27"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急演练_演练开始", "接口异常")

    def test_IM_通讯录组织_一层一层获取(self):
        url_rq = "/txearth/im/get-i-m-contacts"
        data = json.dumps({"org_id": "164"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_通讯录组织_一层一层获取", "接口异常")

    def test_IM_通讯录组织_加入群聊(self):
        url_rq = "/txearth/im/join-group-chat"
        data = json.dumps({"group_id": "chat-85", "members": ["luojunfeng"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_加入群聊", "接口异常")

    def test_IM_通讯录组织_删除群聊用户(self):
        url_rq = "/txearth/im/del-group-chat"
        data = json.dumps({"group_id": "chat-85", "members": ["luojunfeng"]})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_删除群聊用户", "接口异常")

    def test_IM_通过房间id加入房间(self):
        url_rq = "/txearth/im/join-group-by-id"
        data = json.dumps({"group_id": "chat-85"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_通过房间id加入房间", "接口异常")

    def test_IM_获取群成员(self):
        url_rq = "/txearth/im/get-members"
        data = json.dumps({"group_id": "chat-85"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_获取群成员", "接口异常")

    def test_IM_创建群聊(self):
        url_rq = "/txearth/im/create-group-chat"
        data = json.dumps({
            "uid": "2934",
            "members": [
                "111000000000000001",
                "111000000000000002",
                "111000000000000003",
                "111000000000000004"
            ],
            "room_name": "杨疆龙2021-11-04 15:35的一键报警处置",
            "type": 1,
            "id": 153,
            "sos_uid": "2932"
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_创建群聊", "接口异常")

    def test_IM_通讯录搜索(self):
        url_rq = "/txearth/im/get-user-by-name"
        data = json.dumps({"name": "罗俊"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_通讯录搜索", "接口异常")

    def test_IM_通讯录列表_整个组织机构(self):
        url_rq = "/txearth/im/get-i-m-contacts-v2"
        data = json.dumps({"org_id": "164"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("IM_通讯录列表_整个组织机构", "接口异常")

    def test_值班记录_列表(self):
        url_rq = "/txearth/duty-record/record-list"
        data = json.dumps({"name": "", "page": 1, "size": 20})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("值班记录_列表", "接口异常")

    def test_值班记录_详情(self):
        url_rq = "/txearth/duty-record/record-info"
        data = json.dumps({"id": "65"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("值班记录_详情", "接口异常")

    def test_值班记录_获取报警记录(self):
        url_rq = "/txearth/duty-record/get-receive-police"
        data = json.dumps({"id": "65"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("值班记录_获取报警记录", "接口异常")

    def test_值班记录_保存(self):
        url_rq = "/txearth/duty-record/record-save"
        data = json.dumps({
            "leader": "ut labore sint Excepteur",
            "watchman": "officia eiusmod do cillum reprehenderit",
            "duty_date": "2005-02-21",
            "duty_date_end": "2005-02-21",
            "weather": "labore non",
            "content": "proident id esse irure dolore",
            "id": "",
            "mobile": "",
            "handover_date": ""
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("值班记录_保存", "接口异常")

    def test_视频监控_项目列表(self):
        url_rq = "/txearth/monitor/get-project-list"
        data = json.dumps({"name": "", "id": "110"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("视频监控_项目列表", "接口异常")

    def test_视频监控_获取视频(self):
        url_rq = "/txearth/monitor/get-monitor"
        data = json.dumps({"id": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("视频监控_获取视频", "接口异常")

    def test_视频监控_添加摄像头配置(self):
        url_rq = "/txearth/monitor/monitor-add"
        data = json.dumps({"project_id": "1", "rtsp": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("视频监控_添加摄像头配置", "接口异常")

    def test_文件管理_获取文件树(self):
        url_rq = "/txearth/file-management/get-management-tree"
        data = json.dumps({"receive_id": "1", "type": "1"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("文件管理_获取文件树", "接口异常")

    def test_文件管理_列表(self):
        url_rq = "/txearth/emergency/file-management-list"
        data = json.dumps({"receive_id": "290", "file_id": ""})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("文件管理_列表", "接口异常")

    def test_文件管理_添加文件(self):
        url_rq = "/txearth/emergency/file-management-add-file"
        data = json.dumps({
            "file_id": "53",
            "file": [
                {
                    "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir2021111915/1637307076.pdf",
                    "file_name": "安哥拉 国别信息"
                },
                {
                    "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir2021112218/1637576485.pdf",
                    "file_name": "-03W-bO-K1kM_NsApSh38sXTEkY-Biy7.pdf"
                },
                {
                    "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir2021112218/1637576926.pdf",
                    "file_name": "23424234.pdf"
                },
                {
                    "file": "http://dianjian.cc/usr/local/www/php/backend/runtime/earthFile2021112816/1638087925.pdf",
                    "file_name": "wrwerwerwerwer.pdf"
                }
            ]
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("文件管理_添加文件", "接口异常")

    def test_文件管理_创建文件夹(self):
        url_rq = "/txearth/emergency/file-management"
        data = json.dumps({"receive_id": 548, "status": 4, "title": "测试", "file_id": 965})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("文件管理_创建文件夹", "接口异常")

    def test_培训_列表搜索(self):
        url_rq = "/txearth/train/train-list-search"
        data = json.dumps({"name": "中"})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          data=data, verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("培训_列表搜索", "接口异常")

    def test_培训_列表(self):
        url_rq = "/txearth/train/train-list"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("培训_列表", "接口异常")

    def test_应急指挥_周边资源类型(self):
        url_rq = "/txearth/coordinates/neartype"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_周边资源类型", "接口异常")

    def test_应急指挥_人工报警列表(self):
        url_rq = "/txearth/statistics/get-manual-alarm"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_人工报警列表", "接口异常")

    def test_应急指挥_app报警列表(self):
        url_rq = "/txearth/statistics/onekey-alarm"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_app报警列表", "接口异常")

    def test_应急指挥_人员类型(self):
        url_rq = "/txearth/emergency/user-type"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_人员类型", "接口异常")

    def test_应急指挥_事故事件发生地_树状结构(self):
        url_rq = "/txearth/area-list-new/project-isset"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_事故事件发生地_树状结构", "接口异常")

    def test_应急指挥_接警处置记录(self):
        url_rq = "/txearth/statistics/onekey-alarm-more"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,
                                          verify=False)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("应急指挥_接警处置记录", "接口异常")
