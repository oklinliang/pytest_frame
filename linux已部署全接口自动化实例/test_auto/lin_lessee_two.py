import lin_config
import lin_chandao
import json
import requests
import urllib3
import lin_sql_perform
import lin_token

"""
    网页app自动化程序
"""

url = lin_config.request_url
headers = lin_config.request_headers
code = lin_token.html_app_getcode(url,headers)
lin_sql_perform.html_app_login_token(lin_config.my_uid)
my_token,request_token,request_id= lin_token.html_app_login_token(url,headers,code)

class Test_网页app():
    def test_首页_6大区域(self):
        url_rq = "/api/v1.0/dataStatistics/index_"
        data = json.dumps({"req": {},"common": {"uid": 2994}})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("首页_6大区域", "接口异常")

    def test_百万工时_获取项目信息_添加时(self):
        url_rq = "/api/v1.0/workingHours/getProject"
        data = json.dumps({"req": {"id": ""},"common": {"uid": 2994}})
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("百万工时_获取项目信息_添加时", "接口异常")

    def test_百万工时_统计_管理员查看(self):
        url_rq = "/api/v1.0/workingHours/workingHoursStatistics"
        data = json.dumps({
            "req": {
                "investement_child": [],
                "tims": "2021-12",
                "project_name": "",
                "signing": []
            },
            "common": {
                "uid": 2994
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("百万工时_统计_管理员查看", "接口异常")

    def test_百万工时_保存(self):
        url_rq = "/api/v1.0/workingHours/saveWorkingHours"
        data = json.dumps({
            "req": {
                "area_project_id": "4153",
                "month": "2021-12",
                "formal": "1",
                "local": "2",
                "third": "3",
                "death_events": "4",
                "death_events_peoples": "5",
                "no_work_events": "7",
                "no_work_events_peoples": "8",
                "no_work_events_misse": "9",
                "limited_work_events": "10",
                "limited_work_events_peoples": "11",
                "limited_work_events_misse": "12",
                "other_events": "13"
            },
            "common": {
                "uid": 27786
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("百万工时_保存", "接口异常")

    def test_百万工时_记录(self):
        url_rq = "/api/v1.0/workingHours/workingHoursList"
        data = json.dumps({
            "req": {
            "id": "4119"
            },
            "common": {
            "uid": 2994
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("百万工时_记录", "接口异常")

    def test_百万工时_详情(self):
        url_rq = "/api/v1.0/workingHours/workingHoursDetial"
        data = json.dumps({
            "req": {
            "id": "17"
            },
            "common": {
            "uid": 2994
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("百万工时_详情", "接口异常")

    def test_应急资源_创建修改应急组织(self):
        url_rq = "/api/v1.0/emergencyDrillResources/organization"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "type_id": 1,
                "project_id": 2,
                "title": "应急办",
                "contacats": "test",
                "tel": 123,
                "satellite_telephone": "123",
                "id": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_创建修改应急组织", "接口异常")

    def test_应急资源_创建修改应急物资装备(self):
        url_rq = "/api/v1.0/emergencyDrillResources/equipment"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "type": 2,
                "project_id": 2,
                "emergency_supplies_name": "test",
                "number": "123",
                "model": "123",
                "contact_channels": "test",
                "person_liable": "test",
                "tel": "213",
                "satellite_telephone": "23",
                "type_id": 3,
                "type_name": "dasdsa",
                "id": 25
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_创建修改应急物资装备","接口异常")

    def test_应急资源_应急物资装备删除(self):
        url_rq = "/api/v1.0/emergencyDrillResources/deleteEquipment"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "id": "25"
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_应急物资装备删除","接口异常")

    def test_应急资源_获取应急组织列表(self):
        url_rq = "/api/v1.0/emergencyDrillResources/emergencyOrganization"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "id": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_获取应急组织列表","接口异常")

    def test_应急资源_获取应急物资(self):
        url_rq = "/api/v1.0/emergencyDrillResources/emergencySupplies"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "id": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_获取应急物资","接口异常")

    def test_应急资源_应急装备或物资类型(self):
        url_rq = "/api/v1.0/emergencyDrillResources/typeList"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "type": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_应急装备或物资类型","接口异常")

    def test_应急资源_获取应急装备列表(self):
        url_rq = "/api/v1.0/emergencyDrillResources/emergencyEquipment"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "id": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("应急资源_获取应急装备列表","接口异常")

    def test_项目管理_安保信息删除(self):
        url_rq = "/api/v1.0/projectv2/delProjectSecurity"
        data = json.dumps({
            "req": {
                "area_project_id": "3481"
            },
            "common": {
                "uid": 2994
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目管理_安保信息删除", "接口异常")

    def test_项目管理_视频删除(self):
        url_rq = "/api/v1.0/projectv2/delMonitor"
        data = json.dumps({
            "req": {
                "monitor": {
                    "project_id": "",
                    "monitor_id": ""
                }
            },
            "common": {
                "uid": 2994
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目管理_视频删除", "接口异常")

    def test_项目管理_视频保存(self):
        url_rq = "/api/v1.0/projectv2/saveMonitor"
        data = json.dumps({
            "req": {
                "project_id": "4153",
                "project_type": ""
            },
            "common": {
                "platform": "android",
                "token": "",
                "uid": "2994",
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目管理_视频保存", "接口异常")

    def test_项目管理_项目详情(self):
        url_rq = "/api/v1.0/projectv2/lastProjectv2"
        data = json.dumps({
            "req": {
                "project_id": "4153",
                "project_type": ""
            },
            "common": {
                "platform": "android",
                "token": "",
                "uid": "2994",
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目管理_项目详情", "接口异常")

    def test_项目管理_安保信息保存(self):
        url_rq = "/api/v1.0/projectv2/lastProjectv2"
        data = json.dumps({
            "req": {
                "security": {
                    "area_project_id": "3502",
                    "proportion": "",
                    "managers_num": "",
                    "armed_security_num": "",
                    "police_num": "",
                    "local_security_num": "",
                    "chinese_security_num": "",
                    "is_video_system": "",
                    "is_alarms": "",
                    "is_satellite_telephone": "",
                    "satellite_telephone": "",
                    "walkie_talkie_num": "",
                    "is_strong_fence": "",
                    "is_crash_pillar": "",
                    "is_watchtower": "",
                    "is_power_grid": "",
                    "is_sandbag": "",
                    "is_bulletproof_vehicle": "",
                    "capacity": "",
                    "is_living_materials": "",
                    "frequency": "",
                    "last_risk_level": "",
                    "reason": "",
                    "is_early_warning": "",
                    "one_yeay_early_warning": "",
                    "is_emergency_plan": "",
                    "emergency_drill_num": "",
                    "is_high_risk_evacuation": "",
                    "emergency_evacuation_num": "",
                    "evacuate_vehicles": "",
                    "is_embassy_communication": "",
                    "is_IMO_contact": "",
                    "is_police_contact": "",
                    "is_community_relations": "",
                    "is_camp_closure": "",
                    "is_guard": "",
                    "regular_commuting_num": "",
                    "is_regular_commuting": "",
                    "project_risk_level": "",
                    "is_project_armed_conflict": "",
                    "is_country_armed_conflict": "",
                    "is_terrorist_org": "",
                    "terrorist_attacks_num": "",
                    "is_religious_contradiction": "",
                    "is_ethnic_contradiction": "",
                    "personnel_hijacking_num": "",
                    "hijacking_death_num": "",
                    "robberies_num": "",
                    "robbery_outside_num": "",
                    "is_political_situation_stable": "",
                    "is_presidential_election": "",
                    "is_partisan_bickering": "",
                    "country_political_situation_stable": "",
                    "project_negative_reports_num": "",
                    "malicious_smear_report_num": "",
                    "add_user_id": ""
                }
            },
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目管理_安保信息保存", "接口异常")

    def test_项目管理_项目预案(self):
        url_rq = "/api/v1.0/area/areaPlanFile"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "project_id": 3502,
                "file": [
                    {
                        "file_name": "测试",
                        "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir/2021112819/重大自然灾害应急救援预案.pdf"
                    },
                    {
                        "file_name": "测试",
                        "file": "https://dev.tihal.cn:8888/home/earthFile/img/upload/updir/2021112819/重大自然灾害应急救援预案.pdf"
                    }
                ]
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers,
                                          data=data)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("项目管理_项目预案", "接口异常")

    def test_用户管理_显示本企业通讯录_获取人员(self):
        url_rq = "/api/v1.0/userv2/getManByOrg"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "org_id": 103
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_显示本企业通讯录_获取人员","接口异常")

    def test_用户管理_用旧密码修改新密码(self):
        url_rq = "/api/v1.0/user/resetPasswd"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": "cb8423d6c3fefb35cad0c10f334f7e33",
                "uid": "30814",
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "pwd": "dc5371cacbd433cfb31ac5d826589e4b",
                "newPwd": "12QWaszx@",
                "newPwd2": "12QWaszx@"
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_用旧密码修改新密码","接口异常")

    def test_用户管理_忘记密码获取验证码(self):
        url_rq = "/api/v1.0/user/BackCode"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "account": "yjl",
                "email": "136899978@qq.com"
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_忘记密码获取验证码","接口异常")

    def test_用户管理_用户保存_区域_国家_项目_机构联动(self):
        url_rq = "/api/v1.0/project/get-area-project"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "type": 1,
                "id": "31"
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_用户保存_区域_国家_项目_机构联动","接口异常")

    def test_用户管理_显示本企业通讯录(self):
        url_rq = "/api/v1.0/userv2/getAddressBook"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {}
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_显示本企业通讯录","接口异常")

    def test_用户管理_用户搜索下拉(self):
        url_rq = "/api/v1.0/userv2/userParams"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "org_id": 168
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_用户搜索下拉","接口异常")

    def test_用户管理_所属公司下拉框(self):
        url_rq = "/api/v1.0/tenant/getOrgList"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("用户管理_所属公司下拉框", "接口异常")

    def test_用户管理_获取用户密码是否改过(self):
        url_rq = "/api/v1.0/userv2/getUserPwdIsUp"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {}
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_获取用户密码是否改过","接口异常")

    def test_用户管理_用户授权功能_获取角色(self):
        url_rq = "/api/v1.0/userv2/getAuthRole"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {}
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_用户授权功能_获取角色","接口异常")

    def test_用户管理_用户详情(self):
        url_rq = "/api/v1.0/app_tenant/tenantUserInfo"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "user_id": request_id
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_用户详情","接口异常")

    def test_用户管理_显示本企业通讯录_按照人名搜索(self):
        url_rq = "/api/v1.0/userv2/getUserByName"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "name": "合适"
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_显示本企业通讯录_按照人名搜索","接口异常")

    def test_用户管理_企业通讯录修改(self):
        url_rq = "/api/v1.0/organization/updateOrganization"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "parent_org_id": "162",
                "org_name": "test1—orgssss",
                "org_id": 5836,
                "type": 3
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_企业通讯录修改","接口异常")

    def test_用户管理_忘记密码_根据名字跟公司查询账号(self):
        url_rq = "/api/v1.0/user/forgetAccount"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "org_id": "97",
                "account_nick": "测试-林亮"
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_忘记密码_根据名字跟公司查询账号","接口异常")

    def test_用户管理_企业通讯录创建(self):
        url_rq = "/api/v1.0/organization/createOrganization"
        data = json.dumps({
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            },
            "req": {
                "parent_org_id": "5901",
                "org_name": "test——orgss",
                "type": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_企业通讯录创建","接口异常")

    def test_用户管理_获取项目下的用户列表(self):
        url_rq = "/api/v1.0/userv2/getProjectUser"
        data = json.dumps({
            "req": {
                "page": 1,
                "limit": 20,
                "account_no": "",
                "account_nick": "",
                "enterpris": "",
                "role": ""
            },
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_获取项目下的用户列表","接口异常")

    def test_用户管理_获取区域手机号code(self):
        url_rq = "/api/v1.0/user/getMobileCode"
        data = json.dumps({
            "req": {},
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("用户管理_获取区域手机号code","接口异常")

    def test_事件上报_列表(self):
        url_rq = "/api/v1.0/emergency/policeList"
        data = json.dumps({
            "req": {
                "limit": 20,
                "page": 1,
                "project_title": "",
                "area_id": "",
                "country_id": "",
                "child_id": "",
                "type_id": 4
            },
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("事件上报_列表","接口异常")

    def test_事件上报_获取事故类别(self):
        url_rq = "/api/v1.0/emergency/getAccidentType"
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers)
        assert this_test_json.status_code == 200, lin_chandao.add_bug("事件上报_获取事故类别", "接口异常")

    def test_事件上报_详情(self):
        url_rq = "/api/v1.0/emergency/policeInfo"
        data = json.dumps({
            "req": {
                "id": "442"
            },
            "common": {
                "platform": "android",
                "token": request_token,
                "uid": request_id,
                "version": "1.0",
                "vt": "",
                "is_web": 1
            }
        })
        urllib3.disable_warnings()
        this_test_json = requests.request("POST", url + url_rq  , headers=headers, data=data)
        assert this_test_json.status_code == 200,lin_chandao.add_bug("事件上报_详情","接口异常")