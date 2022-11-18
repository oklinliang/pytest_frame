# -*- coding:utf-8 -*-
#每日巡检内容
import time
from HwTestReport import HTMLTestReport
import unittest
import test_cases
import driver
import os
import everyday_mail

dr = driver.dr
if __name__ == '__main__':
    time_ymd = time.strftime("%Y年%m月%d日")
    time_hms = time.strftime("%H时%M分%S秒")
    if(os.path.exists("D://每日巡检记录//" + time_ymd) is False):
        os.mkdir('D:\\每日巡检记录\\' + time_ymd)
    dr.get(driver.ui_url)

    # 山东高速
    #执行测试用例
    suite = unittest.TestSuite()
    test_cases.demo_test_case(suite)
    with open('D:\\每日巡检记录\\' + time_ymd + '\\' + time_hms + '山东高速.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='每日山东高速巡检自动化测试报告',
                                description='测试报告用例',
                                tester='林亮')
        runner.run(suite)
    time.sleep(10)
    #一带一路
    # 执行测试用例
    suite_B_R = unittest.TestSuite()
    test_cases.B_and_R_test_case(suite_B_R)
    with open('D:\\每日巡检记录\\' + time_ymd + '\\' + time_hms + '一带一路.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='每日一带一路巡检自动化测试报告',
                                description='测试报告用例',
                                tester='林亮')
        runner.run(suite_B_R)
    time.sleep(10)
    # 北方工业
    # 执行测试用例
    suite_N_Industrial = unittest.TestSuite()
    test_cases.N_Industrial_test_case(suite_N_Industrial)
    with open('D:\\每日巡检记录\\' + time_ymd + '\\' + time_hms + '北方工业.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='每日北方工业巡检自动化测试报告',
                                description='测试报告用例',
                                tester='林亮')
        runner.run(suite_N_Industrial)
    time.sleep(10)
    # 中交集团
    # 执行测试用例
    suite_China_Traffic = unittest.TestSuite()
    test_cases.China_Traffic_test_case(suite_China_Traffic)
    with open('D:\\每日巡检记录\\' + time_ymd + '\\' + time_hms + '中交集团.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='每日中交集团巡检自动化测试报告',
                                description='测试报告用例',
                                tester='林亮')
        runner.run(suite_China_Traffic)
    time.sleep(10)

    # 鼎昊国际
    # 执行测试用例
    suite_T_Hrisk = unittest.TestSuite()
    test_cases.T_Hrisk_test_case(suite_T_Hrisk)
    with open('D:\\每日巡检记录\\' + time_ymd + '\\' + time_hms + '鼎昊国际.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='每日鼎昊国际巡检自动化测试报告',
                                description='测试报告用例',
                                tester='林亮')
        runner.run(suite_T_Hrisk)
    time.sleep(10)

    driver.dr.quit()
    # everyday_mail.auto_mail("每日自动巡检页面展示情况测试报告",time_ymd,time_hms)

