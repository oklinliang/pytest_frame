from lin_mysql import UsingMysql

"""
    所有sql均在这里维护
"""
def app_login_token(a):
    with UsingMysql() as um:
        um.cursor.execute("UPDATE cmm_login_cache_t SET type = 1 WHERE user_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def html_app_login_token(a):
    with UsingMysql() as um:
        um.cursor.execute("UPDATE cmm_login_cache_t SET type = 2 WHERE user_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def select_app_token(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM cmm_login_cache_t WHERE user_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def receive_police():
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM receive_police GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def fmm_file_management(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM fmm_file_management WHERE receive_id = "+ str(a) +" AND pid = 0 LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def fmm_map_interact_t(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM fmm_map_interact_t WHERE creator = "+ str(a) +"  GROUP BY map_id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def cmm_account_info_t(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM cmm_account_info_t WHERE account_no = '"+ str(a) +"';")
        data = um.cursor.fetchone()
        return data

def im_group():
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM im_group GROUP BY id DESC LIMIT 1")
        data = um.cursor.fetchone()
        return data

def im_group_membership_a(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM im_group_membership WHERE user_account = '"+ a + "' GROUP BY id DESC LIMIT 1")
        data = um.cursor.fetchone()
        return data

def im_group_membership_b(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT count(1) FROM im_group_membership WHERE group_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def user_login_info_count():
    with UsingMysql() as um:
        um.cursor.execute("SELECT count(1) FROM user_login_info;")
        data = um.cursor.fetchone()
        return data

def user_login_info():
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM user_login_info GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data
#网页app用的sql
def delete_my_project(a):
    with UsingMysql() as um:
        um.cursor.execute("UPDATE area_project SET add_user_id = '1' WHERE add_user_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def area_project(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM area_project WHERE add_user_id = "+ str(a) +" LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def area_project_security_a(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                proportion,\
                managers_num,\
                armed_security_num,\
                police_num,\
                local_security_num,\
                chinese_security_num,\
                is_video_system,\
                is_alarms,\
                is_satellite_telephone,\
                satellite_telephone,\
                walkie_talkie_num,\
                is_strong_fence,\
                is_crash_pillar,\
                is_watchtower,\
                is_power_grid,\
                is_sandbag,\
                is_bulletproof_vehicle,\
                capacity,\
                is_living_materials,\
                frequency,\
                last_risk_level,\
                reason,\
                is_early_warning,\
                one_yeay_early_warning,\
                is_emergency_plan,\
                emergency_drill_num,\
                is_high_risk_evacuation,\
                emergency_evacuation_num,\
                evacuate_vehicles,\
                is_embassy_communication,\
                is_IMO_contact,\
                is_police_contact,\
                is_community_relations,\
                is_camp_closure,\
                is_guard,\
                regular_commuting_num,\
                is_regular_commuting,\
                project_risk_level,\
                is_project_armed_conflict,\
                is_country_armed_conflict,\
                is_terrorist_org,\
                terrorist_attacks_num,\
                is_religious_contradiction,\
                is_ethnic_contradiction,\
                personnel_hijacking_num,\
                hijacking_death_num,\
                robberies_num,\
                robbery_outside_num,\
                is_political_situation_stable,\
                is_presidential_election,\
                is_partisan_bickering,\
                country_political_situation_stable,\
                project_negative_reports_num,\
                malicious_smear_report_num\
            FROM\
                area_project_security\
            WHERE\
                area_project_id = "+ str(a) +";"
        )
        data = um.cursor.fetchone()
        return data

def emergency_organization_a(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT title,contacats,tel,satellite_telephone FROM emergency_organization WHERE project_id = "+ str(a) +" GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def emergency_supplies_a(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT emergency_supplies_name,number,person_liable,tel FROM emergency_supplies WHERE project_id = "+ str(a) +" GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def delete_my_working_hours(a):
    with UsingMysql() as um:
        um.cursor.execute("DELETE FROM area_project_working_hours WHERE area_project_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def area_project_working_hours_a(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                formal,\
                LOCAL,\
                third,\
                death_events,\
                death_events_peoples,\
                no_work_events,\
                no_work_events_misse,\
                no_work_events_peoples,\
                limited_work_events,\
                limited_work_events_misse,\
                limited_work_events_peoples,\
                other_events\
            FROM\
                area_project_working_hours\
            WHERE\
                area_project_id = "+ str(a) +";"
        )
        data = um.cursor.fetchone()
        return data

def personal_information_id(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT id FROM area_project_company apc WHERE area_project_id = "+ str(a) +" AND deleted_at IS NULL GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def personal_information_a(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                child_first_party,\
                formal,\
                informal,\
                `local`,\
                permanent_num,\
                permanent_num_one,\
                permanent_num_two,\
                third,\
                unit_id\
            FROM\
                area_project_company\
            WHERE\
                area_project_id = "+ str(a) +"\
            AND deleted_at IS NULL\
            GROUP BY id DESC LIMIT 1;"
            )
        data = um.cursor.fetchone()
        return data

def personal_information_b(a,b):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                area_project_company_id,\
                NAME,\
                phone,\
                satellite_phone,\
                wechat_number\
            FROM\
                area_project_staff\
            WHERE\
                area_project_id = "+ str(a) +"\
            AND type = 2\
            AND area_project_company_id = "+ str(b) +"\
            GROUP BY id DESC LIMIT 1;"
            )
        data = um.cursor.fetchone()
        return data

def personal_information_c(a,b):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                other,\
                zf_four_domestic_inoculation,\
                zf_four_no_domestic_inoculation,\
                zf_three_domestic_inoculation,\
                zf_three_no_domestic_inoculation\
            FROM\
                area_project_material\
            WHERE\
                area_project_id = "+ str(a) +"\
            AND deleted_at IS NULL\
            AND company_id = "+ str(b) +" LIMIT 1;"
            )
        data = um.cursor.fetchone()
        return data

def area_project_material_a(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                mask,\
                glove,\
                test_kit,\
                n95_mask,\
                aq_steril,\
                protective_mask,\
                protective_clothing,\
                liquid_soap,\
                thermometer_gun,\
                goggles,\
                alcohol_disinfectant,\
                safety_check\
            FROM\
                area_project_material\
            WHERE\
                company_id = "+ str(a) +";"
        )
        data = um.cursor.fetchone()
        return data

def area_project_material_b(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                jinhua_qinggan, \
                fangde_no1, \
                lianhua_qingwen, \
                fangguan_no1, \
                feiyan_no1, \
                zhiguan_no1, \
                qingfei_paidu, \
                zhiguan_no2, \
                huashi_baidu, \
                aosi_tawei, \
                abi_duoer, \
                liba_weilin, \
                linsuan_lukui, \
                toubao_fuxinzhi, \
                aqi_meisu, \
                moxishaxing, \
                other_kangjun, \
                duiyixiananjifen, \
                buluofenhuanshi, \
                other_jiere, \
                shufengjiedu, \
                huoxiangzhengqi, \
                pipagao, \
                fufangyansuan, \
                vc, \
                aisizuolun, \
                is_satisfied, \
                is_clinic, \
                clinic_is_satisfied, \
                is_nucleic_acid, \
                zf_doctor, \
                yf_doctor, \
                zf_nurse, \
                yf_nurse\
            FROM\
                area_project_material\
            WHERE\
                company_id = "+ str(a) +";"
        )
        data = um.cursor.fetchone()
        return data

def fmm_tenant_user_t(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM fmm_tenant_user_t WHERE account_id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def area_project_country_id(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT pid FROM area_project WHERE id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def area_project_area_id(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT pid FROM area_project WHERE id = "+ str(a) +";")
        data = um.cursor.fetchone()
        return data

def receive_police_a(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                event_accidents_name,\
                contracting_unit,\
                performance_unit,\
                OWNER,\
                event_local_time,\
                event_accidents_time,\
                event_accidents_address,\
                event_accidents_type,\
                cause_event_accidents,\
                measure_event_accidents,\
                unit_event_accidents,\
                company,\
                contacts,\
                tel_number\
            FROM\
                receive_police\
            WHERE\
                add_user_id = "+ str(a) +"\
            GROUP BY id DESC LIMIT 1;"
        )
        data = um.cursor.fetchone()
        return data

def receive_police_id(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT id FROM receive_police WHERE add_user_id = "+ str(a) +" GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def receive_police_casualties(a,b):
    with UsingMysql() as um:
        um.cursor.execute("SELECT die_tol,injury_tol,loe_tol FROM receive_police_casualties WHERE receive_police_id = "+ str(a) +" AND user_type_id = "+ str(b) +";")
        data = um.cursor.fetchone()
        return data

def police_schedule(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                NAME,\
                casualties,\
                typeofwork_level,\
                sex,\
                age,\
                working_years,\
                education,\
                loss,\
                remarks,\
                user_type_id\
            FROM\
                police_schedule\
            WHERE\
                receive_police_id = "+ str(a) +";"
        )
        data = um.cursor.fetchone()
        return data

def epidmic_situation_id(a):
    with UsingMysql() as um:
        um.cursor.execute("SELECT id FROM epidmic_situation WHERE add_user_id = "+ str(a) +" GROUP BY id DESC LIMIT 1;")
        data = um.cursor.fetchone()
        return data

def epidmic_situation(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
                company_name,\
                company_place,\
                enterpris_id,\
                country_id,\
                company_survey,\
                find,\
                management,\
                problem,\
                fill_company,\
                fill_people,\
                fill_date,\
                phone\
            FROM\
                epidmic_situation\
            WHERE\
                add_user_id = "+ str(a) +"\
            GROUP BY id DESC LIMIT 1;"
        )
        data = um.cursor.fetchone()
        return data

def epidmic_situation_user(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
              user_name,\
              user_country,\
              diagnosis_date,\
              moving_trajectory,\
              physical_condition,\
              user_type,\
              living_place,\
              user_age,\
              case_type,\
              source_of_infection,\
              treatment_place,\
              mentality,\
              close_contact,\
              daily_protection\
            FROM\
              epidmic_situation_user\
            WHERE\
              situation_id = "+ str(a) +"\
            GROUP BY id DESC LIMIT 1"
        )
        data = um.cursor.fetchone()
        return data

def fmm_user_app_sentiment_t(a):
    with UsingMysql() as um:
        um.cursor.execute(
            "SELECT\
              title,\
              country_id,\
              address,\
              time,\
              sentiment_source,\
              contents,\
              sentiment_reflection,\
              negative_effect,\
              take_steps\
            FROM\
              fmm_user_app_sentiment_t\
            WHERE\
              account_id = "+ str(a) +"\
            GROUP BY sentiment_id DESC LIMIT 1"
        )
        data = um.cursor.fetchone()
        return data

def update_receive_police(a):
    with UsingMysql() as um:
        um.cursor.execute("UPDATE receive_police SET `status` = 3 WHERE add_user_id = "+ str(a) +"")
        data = um.cursor.fetchone()
        return data
