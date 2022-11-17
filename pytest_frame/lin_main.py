# -*- coding:utf-8 -*-
import time
import os
import pytest
import lin_mail
import lin_requests

"""
    此自动化框架主入口
    
    

"""

if __name__ == '__main__':
    pwd = 'C:\\Users\\test\\Desktop\\pytest_frame\\'
    time_ymd = time.strftime("%Y年%m月%d日")
    time_hms = time.strftime("%H时%M分%S秒")
    if (os.path.exists("D://xxx//" + time_ymd) is False):
        os.mkdir('D:\\xxx\\' + time_ymd)
    if lin_requests.auto_request() == 0:
        pytest.main(['-s', '-v', pwd + 'lin_lessee.py', '--html=D:\\xxx\\' + time_ymd + '\\' + time_hms + 'xxx.html'])
        lin_mail.auto_mail("每日自动巡检页面展示情况测试报告", time_ymd, time_hms)
    else:
        print("接口错误")

