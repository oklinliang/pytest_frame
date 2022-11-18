import pytest
import lin_mail
import os
import time

if __name__ == '__main__':
    time_ymd = time.strftime("%Y年%m月%d日")
    time_hms = time.strftime("%H时%M分%S秒")
    if not os.path.exists('.//test_html//'+time_ymd):
        os.mkdir('.//test_html//'+time_ymd)
    pytest.main(['-s', '-v','.//lin_lessee.py', '--html=.//test_html//'+time_ymd+'//指挥中心全接口.html'])
    # pytest.main(['-s', '-v','.//lin_lessee_two.py', '--html=.//test_html// '+time_ymd +'//网页app全接口.html'])
    pytest.main(['-s', '-v','.//lin_lessee_three.py', '--html=.//test_html//' + time_ymd + '//指挥中心接口操作流程.html'])
    # pytest.main(['-s', '-v','.//lin_lessee_four.py', '--html=.//test_html//' + time_ymd + '//网页app接口操作流程.html'])
    lin_mail.lin_mail("每日巡检电建系统接口自动化测试报告", time_ymd, time_hms)
