import json
import requests
import lin_chandao
import lin_config
import lin_sql_perform
import lin_token
import time

"""
    指挥中心流程自动化
"""

url = lin_config.request_url
headers = lin_config.request_headers
my_dect_a = lin_sql_perform.cmm_account_info_t(lin_config.my_user)
lin_sql_perform.app_login_token(lin_config.my_uid)
code = lin_token.html_app_getcode(url,headers)
my_token,request_token,request_id= lin_token.html_app_login_token(url,headers,code)

class Test_指挥中心():
    def test_人工报警正常处理流程(self):
        #人工报警
        value1 = '流程自动化业主名称'
        value2 = '流程自动化事故事件发生单位'
        value3 = '流程自动化备注'
        url_rq = "/txearth/emergency/new-leger-add"
        data = json.dumps({
            "owner": value1,
            "event_accidents_name": value2,
            "event_accidents_time": "2022-05-09 10:34:10",
            "country_id": "15",
            "remarks": value3
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
        my_dect = lin_sql_perform.receive_police()
        if(value1 == my_dect['owner'] and value2 == my_dect['event_accidents_name'] and value3 == my_dect['remarks'] and my_dect['status'] == 0):
            #处置变处置中，建立文件夹
            value4 = '测试建立文件夹'
            time_test = time.strftime("%Y-%m-%d")
            value5 = time_test + value4
            url_rq = "/txearth/emergency/file-management"
            data = json.dumps({
                "receive_id": my_dect['id'],
                "status": "4",
                "title": value4
            })
            requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
            my_dect_a = lin_sql_perform.receive_police()
            my_dect_b = lin_sql_perform.fmm_file_management(my_dect['id'])

            if(my_dect_a['status'] == 4 and my_dect_b['title'] == value5):
                #处理结束
                url_rq = "/txearth/emergency/one-key-alarm-end"
                data = json.dumps({
                    "alarm_id": my_dect['id'],
                    "type": "3"
                })
                requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
                my_dect_a_a = lin_sql_perform.receive_police()
                assert my_dect_a_a['status'] == 2,lin_chandao.add_bug('处理完成失败','处理完成时，数据库receive_police表status字段未从4变2')
            else:
                assert 1==2,lin_chandao.add_bug('处置中切换失败','创建文件夹时应将数据库receive_police表status字段未从0变4')
        else:
            assert 1==2,lin_chandao.add_bug('报警流程错误','插入数据库的值与实际值不符')

    def test_人工报警误报流程(self):
        #人工报警
        value1 = '流程自动化业主名称'
        value2 = '流程自动化事故事件发生单位'
        value3 = '流程自动化备注'
        url_rq = "/txearth/emergency/new-leger-add"
        data = json.dumps({
            "owner": value1,
            "event_accidents_name": value2,
            "event_accidents_time": "2022-05-09 10:34:10",
            "country_id": "15",
            "remarks": value3
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
        my_dect = lin_sql_perform.receive_police()
        if(value1 == my_dect['owner'] and value2 == my_dect['event_accidents_name'] and value3 == my_dect['remarks'] and my_dect['status'] == 0):
            url_rq = "/txearth/emergency/update-police-status"
            data = json.dumps({
                "receive_id": my_dect['id'],
                "status": "3"
            })
            requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
            my_dect_a = lin_sql_perform.receive_police()
            assert my_dect_a['status'] == 3,lin_chandao.add_bug('误报失败','误报后，数据库receive_police表status字段应从0变3')
        else:
            assert 1==2,lin_chandao.add_bug('报警流程错误','插入数据库的值与实际值不符')

    def test_位置共享与群聊的发起与结束(self):
        my_dect_a = lin_sql_perform.cmm_account_info_t(lin_config.my_user)
        value1 = '位置共享与群聊的发起与结束房间'
        url_rq = "/txearth/interact/map-interact-add"
        data = json.dumps({
            "police_id": "",
            "type": 1
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,data=data)
        my_dect_b = lin_sql_perform.fmm_map_interact_t(my_dect_a['account_id'])
        if(my_dect_b['status'] == 1):
            url_rq = "/txearth/im/create-group-chat"
            data = json.dumps({
                "uid": my_dect_a['account_id'],
                "members": [],
                "room_name": value1,
                "type": 1,
                "id": "",
                "sos_uid": ""
            })
            requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,data=data)
            my_dect_c = lin_sql_perform.im_group()
            if(my_dect_c['group_name'] == value1):
                url_rq = "/txearth/im/join-group"
                data = json.dumps({"id": my_dect_c['id']})
                requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,data=data)
                my_dect_d = lin_sql_perform.im_group()
                if(my_dect_d['join_id'] == "map-" + str(my_dect_b['map_id'])):
                    url_rq = "/txearth/interact/end-map"
                    data = json.dumps({
                        "receive_police_id": "",
                        "type": 1,
                        "map_id": my_dect_b['map_id']
                    })
                    requests.request("POST", url + url_rq + "?access-token=" + my_token,headers=headers, data=data)
                    my_dect_e = lin_sql_perform.fmm_map_interact_t(my_dect_a['account_id'])
                    assert my_dect_e['status'] == 2,lin_chandao.add_bug("结束位置共享失败","位置共享结束时，数据库内字段未更新")
                else:
                    assert 1 == 2,lin_chandao.add_bug("房间与位置共享绑定失败","数据库内信息未绑定")
            else:
                assert 1 == 2,lin_chandao.add_bug("创建房间失败","创建房间的接口错误")

        else:
            assert 1 == 2,lin_chandao.add_bug("创建位置共享失败","创建位置共享的接口错误")

    def test_群聊房间加人与删人(self):
        my_dect_a = lin_sql_perform.cmm_account_info_t(lin_config.my_user)
        url_rq = "/txearth/interact/map-interact-add"
        data = json.dumps({
            "police_id": "",
            "type": 1
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,data=data)
        my_dect_b = lin_sql_perform.fmm_map_interact_t(my_dect_a['account_id'])
        url_rq = "/txearth/im/create-group-chat"
        data = json.dumps({
            "uid": my_dect_a['account_id'],
            "members": [],
            "room_name": "亮测试群聊房间",
            "type": 1,
            "id": "",
            "sos_uid": ""
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
        my_dect_c = lin_sql_perform.im_group()
        url_rq = "/txearth/im/join-group"
        data = json.dumps({"id": my_dect_c['id']})
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
        user_value = "luojunfeng"
        url_rq = "/txearth/im/join-group-chat"
        data = json.dumps({
            "group_id": my_dect_c['group_id'],
            "members": [
                user_value
            ]
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
        my_dect_d = lin_sql_perform.im_group_membership_a(user_value)
        if(my_dect_d['group_id'] == my_dect_c['id']):
            url_rq = "/txearth/im/del-group-chat"
            data = json.dumps({
                "group_id": my_dect_c['group_id'],
                "members": [
                    "luojunfeng"
                ]
            })
            requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
            my_dect_e = lin_sql_perform.im_group_membership_b(my_dect_c['id'])
            if(my_dect_e['count(1)'] == 1):
                url_rq = "/txearth/interact/end-map"
                data = json.dumps({
                    "receive_police_id": "",
                    "type": 1,
                    "map_id": my_dect_b['map_id']
                })
                requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
                assert 1==1
            else:
                url_rq = "/txearth/interact/end-map"
                data = json.dumps({
                    "receive_police_id": "",
                    "type": 1,
                    "map_id": my_dect_b['map_id']
                })
                requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
                assert 1 == 2,lin_chandao.add_bug("删除用户失败","删除群聊用户时失败")
        else:
            assert 1 == 2,lin_chandao.add_bug("房间加入失败","房间加人失败")

    def test_值班记录新增(self):
        my_dect_a = lin_sql_perform.user_login_info_count()
        value1 = '值班领导框'    #值班领导
        value2 = '值班人员框'    #值班人员
        value3 = '13311113333'  #手机号
        value4 = '晴天'          #天气
        value5 = '测试交接内容'   #内容
        value6 = time.strftime("%Y-%m-%d")
        url_rq = "/txearth/duty-record/record-save"
        data = json.dumps({
            "leader": value1,
            "watchman": value2,
            "mobile": value3,
            "weather": value4,
            "content": value5,
            "duty_date": value6 + " 00:00",
            "duty_date_end": value6 + " 09:03",
            "handover_date": value6 + " 09:03"
        })
        requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers,data=data)
        my_dect_b = lin_sql_perform.user_login_info_count()
        if(my_dect_a['count(1)'] + 1 == my_dect_b['count(1)']):
            my_dect_c = lin_sql_perform.user_login_info()
            assert my_dect_c['mobile'] == value3 and my_dect_c['content'] == value5 and my_dect_c['leader'] == value1 and my_dect_c['watchman'] == value2 and my_dect_c['weather'] == value4,lin_chandao.add_bug("新增值班记录错误","新增值班记录与提交内容不一致")
        else:
            assert 1 == 2,lin_chandao.add_bug("新增值班记录错误","新增值班记录在表内查询不到")

    def test_app报警失败(self):
        lin_sql_perform.update_receive_police(lin_config.my_uid)
        # my_dect_a = lin_sql_perform.cmm_account_info_t(lin_config.my_user)
        url_rq = "/api/v1.0/position/positionReport?from=2&appId=1&vt=1639041468982&sign=eee72d8ea6568c6958c095d6870285ee"
        data = json.dumps({
            "common": {
                "version": "3.0.2",
                "platform": "android",
                "vt": 1639041468982,
                "uid": lin_config.my_uid,
                "token": request_token
            },
            "req": {
                "locationX": "-116.419389",
                "locationY": "34.9592083",
                "locationType": 0,
                "alarmId": 0,
                "alarmType": 0,
                "isOffline": 0,
                "offlineTime": "2022-05-04 21:56",
                "locationXOffline": "116.2815487",
                "locationYOffline": "39.8208002"
            }
        })
        requests.request("POST", url + url_rq, headers=headers,data=data)
        my_dect_b = lin_sql_perform.receive_police()
        if(my_dect_b['add_user_id'] == lin_config.my_uid and my_dect_b['type'] == 1 and my_dect_b['status'] == 0):
            url_rq = "/txearth/emergency/update-police-status"
            data = json.dumps({
                "receive_id": my_dect_b['id'],
                "status": "3"
            })
            requests.request("POST", url + url_rq + "?access-token=" + my_token, headers=headers, data=data)
            my_dect_a = lin_sql_perform.receive_police()
            assert my_dect_a['status'] == 3,lin_chandao.add_bug('误报失败','误报后，数据库receive_police表status字段应从0变3')
        else:
            assert 1 == 2,lin_chandao.add_bug("app报警失败","app报警数据未存入报警表")


