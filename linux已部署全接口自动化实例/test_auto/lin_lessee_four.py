import json
import time
import requests
import lin_chandao
import lin_sql_perform
import lin_config
import lin_token
import random

"""
    网页app流程自动化
"""



url = lin_config.request_url
headers = lin_config.request_headers
my_dict_on = lin_sql_perform.cmm_account_info_t(lin_config.my_user)
lin_sql_perform.html_app_login_token(lin_config.my_uid)
code = lin_token.html_app_getcode(url,headers)
my_token,request_token,request_id= lin_token.html_app_login_token(url,headers,code)
print(my_token)
print(request_token)


class Test_网页app():
    def test_修改填报人(self):
        lin_sql_perform.delete_my_project(lin_config.my_uid)
        project_id="4487"
        url_rq = "/api/v1.0/project/upProjectUser"
        data = json.dumps({
            "req": {
                "account_no": lin_config.my_user,
                "project_id": project_id
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
        requests.request("POST", url + url_rq  , headers=headers, data=data)
        my_dect_a = lin_sql_perform.area_project(lin_config.my_uid)
        assert str(my_dect_a['id']) == project_id,lin_chandao.add_bug("修改填报人失败","修改填报人时报错")

    def test_安保信息保存(self):
        project_id="4487"
        on_time = time.strftime("%Y-%m-%d %H:%M:%S")
        values = [
            str(random.randint(1,99)),#安保费用占合同额或投资额比重（%）
            str(random.randint(1,999)),#具有专业资质的安保管理人员数量（人）
            str(random.randint(1,999)),#项目持枪保安数量（人）
            str(random.randint(1,999)),#项目当地军警数量（人）
            str(random.randint(1,999)),#项目当地保安数量（人）
            str(random.randint(1,999)),#项目中方专职保安数量（人）
            str(random.randint(1,2)),#是否有视频监控系统
            str(random.randint(1,2)),#是否有警报器、围栏传感器
            str(random.randint(1,2)),#是否有卫星电话
            str(random.randint(13000000000,13999999999)),#卫星电话号码
            str(random.randint(1,99)),#对讲机数量
            str(random.randint(1,2)),#是否有坚固围墙
            str(random.randint(1,2)),#是否有防撞柱、防冲撞设施
            str(random.randint(1,2)),#是否有碉楼或瞭望塔
            str(random.randint(1,2)),#围墙是否有电网、铁丝网等
            str(random.randint(1,2)),#是否有沙袋、掩体
            str(random.randint(1,2)),#是否有防弹车
            str(random.randint(1,999)),#避难室或安全屋可容纳人数
            str(random.randint(1,2)),#避难室是否有充足的生活物资
            str(random.randint(1,3)),#每年动态评估项目安全形势频次
            str(random.randint(1,2)),#最近一次评估项目安全风险等级结果
            '测试结果理由',#取得该结果的理由是（50字以内）
            str(random.randint(1,2)),#是否有监测预警机制
            str(random.randint(1,99)),#近一年收到各方监测预警数量
            str(random.randint(1,2)),#是否有应急预案
            str(random.randint(1,99)),#每年开展应急演练、培训频次
            str(random.randint(1,2)),#是否制订高风险地区撤离预案
            str(random.randint(1,99)),#应急撤离线路数量
            str(random.randint(1,5)),#撤离交通工具有哪些
            str(random.randint(1,2)),#是否与使馆建立沟通机制
            str(random.randint(1,2)),#是否与国际海事组织、反海盗中心等建立联系机制
            str(random.randint(1,2)),#是否与当地军警部门建立联系
            str(random.randint(1,2)),#是否与当地社区建立良好关系
            str(random.randint(1,2)),#营地是否实行封闭式管理
            str(random.randint(1,2)),#出行是否配备警卫
            str(random.randint(1,99)),#常规通勤或赴现场线路数量
            str(random.randint(1,2)),#常规通勤时间是否固定
            str(random.randint(1,5)),#项目所处地区风险等级（参照外交标准）单选
            str(random.randint(1,2)),#近一年项目周边是否发生武装冲突
            str(random.randint(1,2)),#近一年周边国家是否发生武装冲突
            str(random.randint(1,2)),#当地是否有恐怖组织存在
            str(random.randint(1,99)),#近一年当地发生恐怖袭击事件数量
            str(random.randint(1,2)),#当地宗教矛盾是否突出
            str(random.randint(1,2)),#当地民族矛盾是否突出
            str(random.randint(1,99)),#近一年项目发生人员劫持事件数量
            str(random.randint(1,99)),#因劫持导致死亡人员数量
            str(random.randint(1,99)),#发生营地设施、物资、设备被抢劫事件数量
            str(random.randint(1,99)),#发生人员外出遭抢劫事件数量
            str(random.randint(1,2)),#当地政局是否平稳
            str(random.randint(1,2)),#近两年内是否有总统大选
            str(random.randint(1,2)),#当地政府党派斗争是否激烈
            str(random.randint(1,2)),#周边国家或地区政局是否平稳
            str(random.randint(1,99)),#近一年发生涉项目负面报道数量
            str(random.randint(1,99))#近一年发生恶意抹黑、反华仇华负面报道数量
        ]
        url_rq = "/api/v1.0/projectv2/saveProjectSecurity"
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
                "security": {
                    "id": "25",
                    "area_project_id": project_id,
                    "proportion": values[0],
                    "managers_num": values[1],
                    "armed_security_num": values[2],
                    "police_num": values[3],
                    "local_security_num": values[4],
                    "chinese_security_num": values[5],
                    "is_video_system": values[6],
                    "is_alarms": values[7],
                    "is_satellite_telephone": values[8],
                    "satellite_telephone": values[9],
                    "walkie_talkie_num": values[10],
                    "is_strong_fence": values[11],
                    "is_crash_pillar": values[12],
                    "is_watchtower": values[13],
                    "is_power_grid": values[14],
                    "is_sandbag": values[15],
                    "is_bulletproof_vehicle": values[16],
                    "capacity": values[17],
                    "is_living_materials": values[18],
                    "frequency": values[19],
                    "last_risk_level": values[20],
                    "reason": values[21],
                    "is_early_warning": values[22],
                    "one_yeay_early_warning": values[23],
                    "is_emergency_plan": values[24],
                    "emergency_drill_num": values[25],
                    "is_high_risk_evacuation": values[26],
                    "emergency_evacuation_num": values[27],
                    "evacuate_vehicles": [values[28]],
                    "is_embassy_communication": values[29],
                    "is_IMO_contact": values[30],
                    "is_police_contact": values[31],
                    "is_community_relations": values[32],
                    "is_camp_closure": values[33],
                    "is_guard": values[34],
                    "regular_commuting_num": values[35],
                    "is_regular_commuting": values[36],
                    "project_risk_level": values[37],
                    "is_project_armed_conflict": values[38],
                    "is_country_armed_conflict": values[39],
                    "is_terrorist_org": values[40],
                    "terrorist_attacks_num": values[41],
                    "is_religious_contradiction": values[42],
                    "is_ethnic_contradiction": values[43],
                    "personnel_hijacking_num": values[44],
                    "hijacking_death_num": values[45],
                    "robberies_num": values[46],
                    "robbery_outside_num": values[47],
                    "is_political_situation_stable": values[48],
                    "is_presidential_election": values[49],
                    "is_partisan_bickering": values[50],
                    "country_political_situation_stable": values[51],
                    "project_negative_reports_num": values[52],
                    "malicious_smear_report_num": values[53],
                    "add_user_id": lin_config.my_uid,
                    "created_at": on_time,
                    "updated_at": on_time,
                    "deleted_at": None
                }
            }
        })
        requests.request("POST", url + url_rq  , headers=headers,data=data)
        my_dict_a = lin_sql_perform.area_project_security_a(project_id)
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all,lin_chandao.add_bug("项目安保信息保存错误","项目安保信息保存与选择不一致")

    def test_项目信息管理员保存(self):
        project_id = "4487"
        values = [
            '测试应急管理员',#部门
            '应急管理员测试',#联系人
            str(random.randint(13000000000,13999999999)),#电话
            str(random.randint(13000000000,13999999999))#卫星电话
        ]
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
                "type_id": "1",
                "project_id": project_id,
                "title": values[0],
                "contacats": values[1],
                "tel": values[2],
                "satellite_telephone": values[3],
                "id": ""
            }
        })
        requests.request("POST", url + url_rq  , headers=headers,data=data)
        my_dict_a = lin_sql_perform.emergency_organization_a(project_id)
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all, lin_chandao.add_bug("项目应急管理员保存错误", "项目应急管理员保存与填写不一致")

    def test_项目应急物资保存(self):
        project_id = 4487
        values = [
            "测试名称",#名称
            str(random.randint(1,999)),#数量
            "测试管理人",#管理人
            str(random.randint(13000000000,13999999999))#联系方式
        ]
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
                "type": "1",
                "project_id": project_id,
                "emergency_supplies_name": values[0],
                "number": values[1],
                "person_liable": values[2],
                "tel": values[3],
                "type_id": "4",
                "type_name": ""
            }
        })
        requests.request("POST", url + url_rq  , headers=headers,data=data)
        my_dict_a = lin_sql_perform.emergency_supplies_a(project_id)
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all, lin_chandao.add_bug("项目应急物资保存错误", "项目应急物资保存与填写不一致")

    def test_项目应急装备保存(self):
        project_id = 4487
        values = [
            "测试警戒类名称",#名称
            str(random.randint(1,999)),#数量
            "测试警戒累管理员",#管理人
            str(random.randint(13000000000,13999999999))#联系方式
        ]
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
                "type": "2",
                "project_id": project_id,
                "emergency_supplies_name": values[0],
                "number": values[1],
                "person_liable": values[2],
                "tel": values[3],
                "type_id": "21",
                "type_name": ""
            }
        })
        requests.request("POST", url + url_rq  , headers=headers,data=data)
        my_dict_a = lin_sql_perform.emergency_supplies_a(project_id)
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all, lin_chandao.add_bug("项目应急装备保存错误", "项目应急装备保存与填写不一致")

    def test_百万工时创建(self):
        project_id = 4487
        on_time = time.strftime("%Y-%m")
        lin_sql_perform.delete_my_working_hours(project_id)
        values = [
            str(random.randint(1,999)),#中方员工
            str(random.randint(1,999)),#本地员工
            str(random.randint(1,999)),#第三国员工
            str(random.randint(1,99)),#死亡事件数
            str(random.randint(1,999)),#死亡事件人数
            str(random.randint(1,99)),#无法工作事件数
            str(random.randint(1,30)),#无法工作事件误工天数
            str(random.randint(1,999)),#无法工作事件人数
            str(random.randint(1,99)),#工作受限的事件数
            str(random.randint(1,30)),#工作受限的事件误工天数
            str(random.randint(1,999)),#工作受限的事件人数
            str(random.randint(1,99))#其他应记录事件数
            ]
        url_rq = "/api/v1.0/workingHours/saveWorkingHours"
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
                "area_project_id": project_id,
                "month": on_time,
                "formal": values[0],
                "local": values[1],
                "third": values[2],
                "death_events": values[3],
                "death_events_peoples": values[4],
                "no_work_events": values[5],
                "no_work_events_misse": values[6],
                "no_work_events_peoples": values[7],
                "limited_work_events": values[8],
                "limited_work_events_misse": values[9],
                "limited_work_events_peoples": values[10],
                "other_events": values[11]
            }
        })
        requests.request("POST", url + url_rq  , headers=headers,data=data)
        my_dict_a = lin_sql_perform.area_project_working_hours_a(project_id)
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all, lin_chandao.add_bug("百万工时保存错误", "百万工时保存与填写不一致")

    def test_人员信息保存(self):
        project_id = 4487
        values1 = [
            '中国水电建设集团国际工程有限公司',#合同甲方
            str(random.randint(1000,9999)),#子企业人数正式
            str(random.randint(1000,9999)),#子企业人数分包
            str(random.randint(1000,9999)),#子企业人数当地
            str(random.randint(10000, 99999)),#常驻超期人数总人数
            str(random.randint(10000, 99999)),#常驻超期人数一年以上
            str(random.randint(10000, 99999)),#常驻超期人数两年以上
            str(random.randint(1000, 9999)),#子企业人数第三国
            '12'
        ]
        values2 = [
            '5963',
            '测试姓名',#项目联络人姓名
            str(random.randint(13000000000, 13999999999)),#项目联络人电话
            str(random.randint(13000000000, 13999999999)),#项目联络人卫星电话
            '测试微信号'#项目联络人微信号
        ]
        values3 = [
            '测试备注',#子企业备注
            str(random.randint(1, 99)),#第四针中方接种国产疫苗人数
            str(random.randint(1, 99)),#第四针中方接种非国产疫苗人数
            str(random.randint(1, 99)),#第三针中方接种国产疫苗人数
            str(random.randint(1, 99))#第三针中方接种非国产疫苗人数
        ]
        url_rq = "/api/v1.0/project/upProjectCompany"
        data = json.dumps({
            "req": {
                "project_id": project_id,
                "type": 1,
                "company_id": values2[0],
                "unit_id": values1[8],
                "other": values3[0],
                "zf_three_domestic_inoculation": values3[3],
                "zf_three_no_domestic_inoculation": values3[4],
                "zf_four_domestic_inoculation": values3[1],
                "zf_four_no_domestic_inoculation": values3[2],
                "child_first_party": values1[0],
                "formal": values1[1],
                "informal": values1[2],
                "local": values1[3],
                "third": values1[7],
                "permanent_num": values1[4],
                "permanent_num_one": values1[5],
                "permanent_num_two": values1[6],
                "person": {
                    "enterpris_person_charge": "",
                    "project_leader": "测试项目经理",
                    "production_leader": "测试生产副经理",
                    "engineer": "测试总工程师",
                    "inspector": "测试安全总监"
                },
                "project_liaison_person_name": values2[1],
                "project_liaison_person_phone": values2[2],
                "satellite_phone": values2[3],
                "wechat_number": values2[4]
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
        requests.request("POST", url + url_rq  , headers=headers,data=data)
        company_id = lin_sql_perform.personal_information_id(project_id)
        my_dict_a = lin_sql_perform.personal_information_a(project_id)
        sql_list_a = list(my_dict_a.values())
        sql_all_a = [str(x) for x in sql_list_a]
        my_dict_b = lin_sql_perform.personal_information_b(project_id,company_id['id'])
        sql_list_b = list(my_dict_b.values())
        sql_all_b = [str(x) for x in sql_list_b]
        my_dict_c = lin_sql_perform.personal_information_c(project_id,company_id['id'])
        sql_list_c = list(my_dict_c.values())
        sql_all_c = [str(x) for x in sql_list_c]
        assert values1 == sql_all_a and values2 == sql_all_b and values3 == sql_all_c, lin_chandao.add_bug("人员信息保存错误", "人员信息保存与填写不一致")

    def test_物资信息保存(self):
        project_id = 4487
        company_id = lin_sql_perform.personal_information_id(project_id)
        values = [
            str(random.randint(1, 9999)),#防护口罩
            str(random.randint(1, 9999)),#检查手套
            str(random.randint(1, 9999)),#新冠肺炎试剂
            str(random.randint(1, 9999)),#N95口罩
            str(random.randint(1, 9999)),#消毒水
            str(random.randint(1, 9999)),#防护面罩
            str(random.randint(1, 9999)),#防护服
            str(random.randint(1, 9999)),#消毒洗手液
            str(random.randint(1, 9999)),#手持测温枪
            str(random.randint(1, 9999)),#护目镜
            str(random.randint(1, 9999)),#酒精消毒液
            str(random.randint(1, 9999))#测温安检门
        ]
        url_rq = "/api/v1.0/project/upProjectCompany"
        data = json.dumps({
            "req": {
                "project_id": project_id,
                "type": 2,
                "company_id": company_id['id'],
                "material": {
                    "mask": values[0],
                    "glove": values[1],
                    "test_kit": values[2],
                    "n95_mask": values[3],
                    "aq_steril": values[4],
                    "protective_mask": values[5],
                    "protective_clothing": values[6],
                    "liquid_soap": values[7],
                    "thermometer_gun": values[8],
                    "goggles": values[9],
                    "alcohol_disinfectant": values[10],
                    "safety_check": values[11]
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
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.area_project_material_a(company_id['id'])
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all, lin_chandao.add_bug("物资信息保存错误", "物资信息保存与填写不一致")

    def test_药品信息保存(self):
        project_id = 4487
        company_id = lin_sql_perform.personal_information_id(project_id)
        values = [
            str(random.randint(1, 100)),#金花清感颗粒
            str(random.randint(1, 100)),#防德一号
            str(random.randint(1, 100)),#连花清瘟
            str(random.randint(1, 100)),#防冠一号
            str(random.randint(1, 100)),#透解祛瘟颗粒
            str(random.randint(1, 100)),#治冠一号
            str(random.randint(1, 100)),#清肺排毒颗粒
            str(random.randint(1, 100)),#治冠二号
            str(random.randint(1, 100)),#化湿败毒颗粒
            str(random.randint(1, 100)),#奥司他韦胶囊
            str(random.randint(1, 100)),#阿比多尔
            str(random.randint(1, 100)),#利巴韦林颗粒
            str(random.randint(1, 100)),#磷酸氯喹
            str(random.randint(1, 100)),#头孢呋辛酯胶囊
            str(random.randint(1, 100)),#阿奇霉素分散片
            str(random.randint(1, 100)),#莫西沙星片
            str(random.randint(1, 100)),#其他抗菌药
            str(random.randint(1, 100)),#对乙酰氨基酚片
            str(random.randint(1, 100)),#布洛芬缓释胶囊
            str(random.randint(1, 100)),#其他解热退烧药
            str(random.randint(1, 100)),#疏风解毒胶囊
            str(random.randint(1, 100)),#藿香正气胶囊
            str(random.randint(1, 100)),#蜜炼川贝枇杷膏
            str(random.randint(1, 100)),#复方盐酸伪麻黄碱缓释胶囊
            str(random.randint(1, 100)),#维生素C片
            str(random.randint(1, 100)),#艾司唑仑片
            '1',#药品是否满足要求
            '1',#是否有医务室
            '1',#医务室是否满足国资委要求
            '1',#是否有核酸检测设备
            str(random.randint(1, 100)),#中方医生
            str(random.randint(1, 100)),#外方医生
            str(random.randint(1, 100)),#中方护士
            str(random.randint(1, 100))#外方护士
        ]
        url_rq = "/api/v1.0/project/upProjectCompany"
        data = json.dumps({
            "req": {
                "project_id": project_id,
                "type": 3,
                "company_id": company_id['id'],
                "drugs": [
                    {
                        "title": "预防类中药",
                        "value": [
                            {
                                "title": "金花清感颗粒",
                                "unit": "6袋/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "jinhua_qinggan",
                                "value": values[0]
                            },
                            {
                                "title": "防德一号",
                                "unit": "2小袋/付，10小袋/中包",
                                "img": None,
                                "status": "1",
                                "reserve": "2",
                                "reserve_unit": "袋",
                                "key": "fangde_no1",
                                "value": values[1]
                            },
                            {
                                "title": "连花清瘟",
                                "unit": "24粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "lianhua_qingwen",
                                "value": values[2]
                            },
                            {
                                "title": "防冠一号",
                                "unit": "7盒/疗程或7袋/中包",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "fangguan_no1",
                                "value": values[3]
                            }
                        ]
                    },
                    {
                        "title": "治疗类中药",
                        "value": [
                            {
                                "title": "透解袪瘟颗粒",
                                "unit": "12袋/包",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "袋",
                                "key": "feiyan_no1",
                                "value": values[4]
                            },
                            {
                                "title": "治冠一号",
                                "unit": "6小袋/疗程",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "疗程",
                                "key": "zhiguan_no1",
                                "value": values[5]
                            },
                            {
                                "title": "清肺排毒颗粒",
                                "unit": "6剂/包",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "包",
                                "key": "qingfei_paidu",
                                "value": values[6]
                            },
                            {
                                "title": "治冠二号",
                                "unit": "12小袋/中包",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "包",
                                "key": "zhiguan_no2",
                                "value": values[7]
                            },
                            {
                                "title": "化湿败毒颗粒",
                                "unit": "12袋/包",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "包",
                                "key": "huashi_baidu",
                                "value": values[8]
                            }
                        ]
                    },
                    {
                        "title": "抗病毒药（至少储备一种）",
                        "value": [
                            {
                                "title": "奥司他韦胶囊",
                                "unit": "6粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "aosi_tawei",
                                "value": values[9]
                            },
                            {
                                "title": "阿比多尔",
                                "unit": "12片/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "abi_duoer",
                                "value": values[10]
                            },
                            {
                                "title": "利巴韦林颗粒",
                                "unit": "18袋/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "liba_weilin",
                                "value": values[11]
                            },
                            {
                                "title": "磷酸氯喹",
                                "unit": "100片/瓶",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "linsuan_lukui",
                                "value": values[12]
                            }
                        ]
                    },
                    {
                        "title": "抗菌类（至少储备一种，亦可选择储备其他同级别药物）",
                        "value": [
                            {
                                "title": "头孢呋辛酯胶囊",
                                "unit": "12粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "toubao_fuxinzhi",
                                "value": values[13]
                            },
                            {
                                "title": "阿奇霉素分散片",
                                "unit": "12片/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "aqi_meisu",
                                "value": values[14]
                            },
                            {
                                "title": "莫西沙星片",
                                "unit": "3片/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "moxishaxing",
                                "value": values[15]
                            },
                            {
                                "title": "其他抗菌药",
                                "unit": "10",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "other_kangjun",
                                "value": values[16]
                            }
                        ]
                    },
                    {
                        "title": "解热退烧药（至少储备一种）",
                        "value": [
                            {
                                "title": "对乙酰氨基酚片",
                                "unit": "10片/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "duiyixiananjifen",
                                "value": values[17]
                            },
                            {
                                "title": "布洛芬缓释胶囊",
                                "unit": "24粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "buluofenhuanshi",
                                "value": values[18]
                            },
                            {
                                "title": "其他解热退烧药",
                                "unit": "10",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "other_jiere",
                                "value": values[19]
                            }
                        ]
                    },
                    {
                        "title": "其他药品",
                        "value": [
                            {
                                "title": "疏风解毒胶囊",
                                "unit": "48粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "shufengjiedu",
                                "value": values[20]
                            },
                            {
                                "title": "藿香正气胶囊",
                                "unit": "16粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "huoxiangzhengqi",
                                "value": values[21]
                            },
                            {
                                "title": "蜜炼川贝枇杷膏",
                                "unit": "120ML/瓶",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "瓶",
                                "key": "pipagao",
                                "value": values[22]
                            },
                            {
                                "title": "复方盐酸伪麻黄碱缓释胶囊",
                                "unit": "10粒/盒",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "盒",
                                "key": "fufangyansuan",
                                "value": values[23]
                            },
                            {
                                "title": "维生素C片",
                                "unit": "100片/瓶",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "瓶",
                                "key": "vc",
                                "value": values[24]
                            },
                            {
                                "title": "艾司唑仑片",
                                "unit": "100片/瓶",
                                "img": None,
                                "status": "1",
                                "reserve": "10",
                                "reserve_unit": "瓶",
                                "key": "aisizuolun",
                                "value": values[25]
                            }
                        ]
                    }
                ],
                "material": {
                    "is_satisfied": values[26],
                    "supply_explain": None,
                    "purchase_drugs": None,
                    "reserve_desc": None,
                    "is_supply": "0",
                    "arrive_desc": None,
                    "is_clinic": values[27],
                    "zf_doctor": values[30],
                    "yf_doctor": values[31],
                    "zf_nurse": values[32],
                    "yf_nurse": values[33],
                    "is_nucleic_acid": values[28],
                    "clinic_is_satisfied": values[29]
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
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.area_project_material_b(company_id['id'])
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]
        assert values == sql_all, lin_chandao.add_bug("药品信息保存错误", "药品信息保存与填写不一致")

    def test_添加修改及删除用户信息(self):
        values = [
            'test_auto',
            '自动化测试',
            str(random.randint(13000000000, 13999999999)),
            str(random.randint(13000000000, 13999999999))
        ]
        url_rq = "/api/v1.0/app_tenant/saveTenantUser"
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
                "org_id": 5874,
                "account_no": values[0],
                "account_nick": values[1],
                "area_id": "",
                "country_id": "",
                "phone1": values[2]
            }
        })
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.cmm_account_info_t(values[0])
        if (my_dict_a['status'] == 1):
            url_rq = "/api/v1.0/app_tenant/saveTenantUser"
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
                    "org_id": 5872,
                    "account_id": my_dict_a['account_id'],
                    "account_no": values[0],
                    "account_nick": values[1],
                    "area_id": "",
                    "country_id": "",
                    "project_id": "",
                    "child_org_id": "",
                    "phone1": values[3],
                    "phone4": None,
                    "email": "",
                    "code4": "",
                    "project_department": "",
                    "passport_no": "",
                    "ID_no": ""
                }
            })
            requests.request("POST", url + url_rq, headers=headers, data=data)
            my_dict_b = lin_sql_perform.fmm_tenant_user_t(my_dict_a['account_id'])
            if(values[3] == my_dict_b['phone1']):
                url_rq = "/api/v1.0/userv2/DelUser"
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
                        "account_id": my_dict_a['account_id']
                    }
                })
                requests.request("POST", url + url_rq, headers=headers, data=data)
                my_dict_c = lin_sql_perform.cmm_account_info_t(values[0])
                assert my_dict_c['status'] == 0,lin_chandao.add_bug("用户删除失败","用户删除后，用户角色表状态未更成失败")
            else:
                assert 1 == 2, lin_chandao.add_bug("用户修改失败", "用户修改入数据库失败")
        else:
            assert 1 == 2,lin_chandao.add_bug("用户添加失败","用户添加入数据库失败")

    def test_项目人员添加修改及删除用户信息(self):
        values = [
            'test_xiangmurenyuan',
            '项目人员添加测试',
            str(random.randint(13000000000, 13999999999)),
            str(random.randint(13000000000, 13999999999))
        ]
        url_rq = "/api/v1.0/app_tenant/saveTenantUser"
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
                "org_id": 5878,
                "account_no": values[0],
                "account_nick": values[1],
                "area_id": "2",
                "country_id": "3",
                "project_id": 3607,
                "phone1": values[2]
            }
        })
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.cmm_account_info_t(values[0])
        if (my_dict_a['status'] == 1):
            url_rq = "/api/v1.0/app_tenant/saveTenantUser"
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
                    "org_id": 5878,
                    "account_id": my_dict_a['account_id'],
                    "account_no": values[0],
                    "account_nick": values[1],
                    "area_id": "2",
                    "country_id": "3",
                    "project_id": "3607",
                    "child_org_id": "",
                    "phone1": values[3],
                    "phone4": None,
                    "email": "",
                    "code4": "",
                    "project_department": "",
                    "passport_no": "",
                    "ID_no": ""
                }
            })
            requests.request("POST", url + url_rq, headers=headers, data=data)
            my_dict_b = lin_sql_perform.fmm_tenant_user_t(my_dict_a['account_id'])
            if(values[3] == my_dict_b['phone1']):
                url_rq = "/api/v1.0/userv2/DelUser"
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
                        "account_id": my_dict_a['account_id']
                    }
                })
                requests.request("POST", url + url_rq, headers=headers, data=data)
                my_dict_c = lin_sql_perform.cmm_account_info_t(values[0])
                assert my_dict_c['status'] == 0,lin_chandao.add_bug("项目人员用户删除失败","项目人员用户删除后，用户角色表状态未更成失败")
            else:
                assert 1 == 2, lin_chandao.add_bug("项目人员用户修改失败", "项目人员用户修改入数据库失败")
        else:
            assert 1 == 2,lin_chandao.add_bug("项目人员用户添加失败","项目人员用户添加入数据库失败")

    def test_驻外机构人员添加修改及删除用户信息(self):
        values = [
            'test_zhuwaijigou',
            '驻外机构人员测试',
            str(random.randint(13000000000, 13999999999)),
            str(random.randint(13000000000, 13999999999))
        ]
        url_rq = "/api/v1.0/app_tenant/saveTenantUser"
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
                "org_id": 5877,
                "account_no": values[0],
                "account_nick": values[1],
                "area_id": "31",
                "country_id": "60",
                "child_org_id": 4156,
                "phone1": values[2]
            }
        })
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.cmm_account_info_t(values[0])
        if (my_dict_a['status'] == 1):
            url_rq = "/api/v1.0/app_tenant/saveTenantUser"
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
                    "org_id": 5877,
                    "account_id": my_dict_a['account_id'],
                    "account_no": values[0],
                    "account_nick": values[1],
                    "area_id": "31",
                    "country_id": "60",
                    "project_id": "",
                    "child_org_id": "4156",
                    "phone1": values[3],
                    "phone4": None,
                    "email": "",
                    "code4": "",
                    "project_department": "",
                    "passport_no": "",
                    "ID_no": ""
                }
            })
            requests.request("POST", url + url_rq, headers=headers, data=data)
            my_dict_b = lin_sql_perform.fmm_tenant_user_t(my_dict_a['account_id'])
            if(values[3] == my_dict_b['phone1']):
                url_rq = "/api/v1.0/userv2/DelUser"
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
                        "account_id": my_dict_a['account_id']
                    }
                })
                requests.request("POST", url + url_rq, headers=headers, data=data)
                my_dict_c = lin_sql_perform.cmm_account_info_t(values[0])
                assert my_dict_c['status'] == 0,lin_chandao.add_bug("驻外机构人员用户删除失败","驻外机构人员用户删除后，用户角色表状态未更成失败")
            else:
                assert 1 == 2, lin_chandao.add_bug("驻外机构人员用户修改失败", "驻外机构人员用户修改入数据库失败")
        else:
            assert 1 == 2,lin_chandao.add_bug("驻外机构人员用户添加失败","驻外机构人员用户添加入数据库失败")

    def test_事件填报信息报送(self):
        project_id = 3607
        country_id = lin_sql_perform.area_project_country_id(project_id)
        area_id = lin_sql_perform.area_project_area_id(country_id['pid'])
        values1 = [
            "测试事故详细名称",  # 事故发生单位详细名称
            "测试总包单位详细名称",  # 签约单位或总包单位详细名称
            "测试实施单位详细名称",  # 委托实施单位详细名称
            "测试业主名称",  # 业主名称
            str(time.strftime("%Y-%m-%d")),  # 当地时间
            str(time.strftime("%Y-%m-%d")),  # 北京时间
            "测试事故发生地点",  # 事故发生地点
            "2",  # 事故类型
            "测试分析",  # 事故的经过和初步原因分析
            "测试应急措施和其他情况",  # 事故发生后采取的应急措施和其他情况
            "测试相关有关情况",  # 事故发生单位概况及其它相关有关情况
            "个人",  # 填报单位
            "测试下",  # 联系人
            str(random.randint(13000000000, 13999999999))  # 联系电话
        ]
        values2 = [
            str(random.randint(1, 100)),  # 中方员工死亡
            str(random.randint(1, 100)),  # 中方员工受伤
            str(random.randint(1, 100)),  # 中方员工失踪
        ]
        values3 = [
            str(random.randint(1, 100)),  # 当地员工死亡
            str(random.randint(1, 100)),  # 当地员工受伤
            str(random.randint(1, 100)),  # 当地员工失踪
        ]
        values4 = [
            str(random.randint(1, 100)),  # 分包员工死亡
            str(random.randint(1, 100)),  # 分包员工受伤
            str(random.randint(1, 100)),  # 分包员工失踪
        ]
        values5 = [
            "测试姓名",  # 姓名
            "暂时没事",  # 伤害情况
            "测试工种级别",  # 工种及级别
            str(random.randint(1, 2)),  # 性别
            str(random.randint(18, 60)),  # 年龄
            str(random.randint(1, 18)),  # 本工龄年龄
            "没有安全教育",  # 受过何种安全教育
            "20",  # 估计直接经济损失
            "没有备注",  # 备注
            str(random.randint(1, 3)),  # 员工类型
        ]
        url_rq = "/api/v1.0/emergency/LedgerAdd"
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
                "event_accidents_name": values1[0],
                "contracting_unit": values1[1],
                "performance_unit": values1[2],
                "owner": values1[3],
                "event_accidents_address": values1[6],
                "event_accidents_time": values1[5],
                "event_accidents_type": values1[7],
                "event_local_time": values1[4],
                "nature": "",
                "cause_event_accidents": values1[8],
                "measure_event_accidents": values1[9],
                "unit_event_accidents": values1[10],
                "remarks": "",
                "area_id": area_id,
                "country_id": country_id,
                "project_id": project_id,
                "company": values1[11],
                "contacts": values1[12],
                "tel_number": values1[13],
                "people": [
                    {
                        "name": values5[0],
                        "casualties": values5[1],
                        "typeofwork_level": values5[2],
                        "sex": values5[3],
                        "age": values5[4],
                        "working_years": values5[5],
                        "education": values5[6],
                        "loss": values5[7],
                        "remarks": values5[8],
                        "cause_event_accidents": "",
                        "user_type_id": values5[9],
                        "close_contact": "",
                        "living_place": "",
                        "epidmic_situation_user": ""
                    }
                ],
                "die": [
                    {
                        "injury_tol": values2[1],
                        "die_tol": values2[0],
                        "loe_tol": values2[2],
                        "user_type_id": 1
                    },
                    {
                        "injury_tol": values3[1],
                        "die_tol": values3[0],
                        "loe_tol": values3[2],
                        "user_type_id": 2
                    },
                    {
                        "injury_tol": values4[1],
                        "die_tol": values4[0],
                        "loe_tol": values4[2],
                        "user_type_id": 3
                    }
                ],
                "country_projects": [],
                "lat": 0,
                "lng": 0
            }
        })
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.receive_police_a(lin_config.my_uid)
        sql_list_a = list(my_dict_a.values())
        sql_all_a = [str(x) for x in sql_list_a]
        receive_police_id = lin_sql_perform.receive_police_id(lin_config.my_uid)
        zf_tol = lin_sql_perform.receive_police_casualties(receive_police_id['id'],'1')
        zf_tol_a = list(zf_tol.values())
        zf_tol_all_a = [str(x) for x in zf_tol_a]
        dd_tol = lin_sql_perform.receive_police_casualties(receive_police_id['id'],'2')
        dd_tol_a = list(dd_tol.values())
        dd_tol_all_a = [str(x) for x in dd_tol_a]
        fb_tol = lin_sql_perform.receive_police_casualties(receive_police_id['id'],'3')
        fb_tol_a = list(fb_tol.values())
        fb_tol_all_a = [str(x) for x in fb_tol_a]
        my_dict_b = lin_sql_perform.police_schedule(receive_police_id['id'])
        sql_list_b = list(my_dict_b.values())
        sql_all_b = [str(x) for x in sql_list_b]
        assert values1 == sql_all_a and values2 == zf_tol_all_a and values3 == dd_tol_all_a and values4 == fb_tol_all_a and values5 == sql_all_b, lin_chandao.add_bug("事件填报信息保存错误", "事件填报信息保存与填写不一致")

    def test_舆情报送上报(self):
        values = [
            "测试舆情标题",  #舆情标题
            "7",  #舆情国家
            "测试舆情地点",  #舆情地点
            str(time.strftime("%Y-%m-%d 00:00:00")),  #舆情时间
            "测试舆情来源",  #舆情来源
            "测试舆情内容",  #舆情内容
            "测试当地反应",  #当地反应
            "测试负面影响",  #负面影响
            "测试采取措施"  #采取措施
        ]
        url_rq = "/api/v1.0/sentiment/sentimentReport"
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
                "title": values[0],
                "countryId": values[1],
                "address": values[2],
                "time": values[3],
                "sentimentSource": values[4],
                "contents": values[5],
                "sentimentReflection": values[6],
                "negativeEffect": values[7],
                "takeSteps": values[8],
                "lat": 0,
                "lng": 0
            }
        })
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.fmm_user_app_sentiment_t(lin_config.my_uid)
        sql_list = list(my_dict_a.values())
        sql_all = [str(x) for x in sql_list]

        assert sql_all == values,lin_chandao.add_bug("舆情报送填报信息保存错误", "舆情报送填报信息保存与填写不一致")

    def test_疫情报送填报信息(self):
        values1 = [
            "测试单位名称",  #单位名称
            "测试单位地点",  #单位地点
            "11",  #子企业
            "10",  #国别
            "测试单位概况",  #单位概况
            "测试病例发现经过及相关原因分析",  #疑似/确诊病例发现经过及相关原因分析
            "测试病例发现后处置情况",  #疑似/确诊病例发现后处置情况
            "测试存在的困难和需要协调解决的问题",  #存在的困难和需要协调解决的问题
            "测试填报单位",  #填报单位
            "测试联系人",  #联系人
            str(time.strftime("%Y-%m-%d 00:00:00")),  #填报时间
            str(random.randint(13000000000,13999999999))
        ]
        values2 = [
            "测试姓名",  #姓名
            "测试国籍",  #国籍
            str(time.strftime("%Y-%m-%d 00:00:00")),  #确诊时间
            "测试移动轨迹过程",  #移动轨迹过程
            "测试身体状况",  #身体状况
            str(random.randint(1,4)),  #人员类型
            "测试生活场所处置情况",  #生活场景处置情况
            str(random.randint(1,60)),  #年龄
            str(random.randint(1,2)),  #病例类型
            "测试传染源",  #传染源
            "测试治疗地点",  #治疗地点
            "测试精神状态",  #精神状态
            "测试密接人员情况",  #密切接触人员情况
            "测试单位日常防护情况"  #所在单位日常防护情况
        ]
        url_rq = "/api/v1.0/epidemic/addPlagueV2"
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
                "company_name": values1[0],
                "company_place": values1[1],
                "company_survey": values1[4],
                "find": values1[5],
                "management": values1[6],
                "problem": values1[7],
                "fill_company": values1[8],
                "fill_date": values1[10],
                "fill_people": values1[9],
                "phone": values1[11],
                "country_id": values1[3],
                "enterpris_id": values1[2],
                "project_name": "",
                "project_place": "",
                "confirmed_time": values1[10],
                "new_cure_time": values1[10],
                "remarks": "",
                "user_name": [
                    values2[0]
                ],
                "user_age": [
                    values2[7]
                ],
                "user_country": [
                    values2[1]
                ],
                "case_type": [
                    values2[8]
                ],
                "diagnosis_date": [
                    values2[2]
                ],
                "source_of_infection": [
                    values2[9]
                ],
                "moving_trajectory": [
                    values2[3]
                ],
                "treatment_place": [
                    values2[10]
                ],
                "physical_condition": [
                    values2[4]
                ],
                "mentality": [
                    values2[11]
                ],
                "user_type": [
                    values2[5]
                ],
                "close_contact": [
                   values2[12]
                ],
                "living_place": [
                    values2[6]
                ],
                "daily_protection": [
                    values2[13]
                ]
            }
        })
        requests.request("POST", url + url_rq, headers=headers, data=data)
        my_dict_a = lin_sql_perform.epidmic_situation(lin_config.my_uid)
        sql_list_a = list(my_dict_a.values())
        sql_all_a = [str(x) for x in sql_list_a]
        epidmic_situation_id = lin_sql_perform.epidmic_situation_id(lin_config.my_uid)
        my_dict_b = lin_sql_perform.epidmic_situation_user(epidmic_situation_id['id'])
        sql_list_b = list(my_dict_b.values())
        sql_all_b = [str(x) for x in sql_list_b]
        assert sql_all_a == values1 and sql_all_b == values2,lin_chandao.add_bug("疫情报送填报信息保存错误", "疫情报送填报信息保存与填写不一致")