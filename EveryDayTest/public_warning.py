import time
import re
import unittest
import driver
import datetime
import request_test

dr = driver.dr
day1 = str(datetime.datetime.now().date())
day2 = "2016-11-09"
timestamp_day1 = int(time.mktime(time.strptime(day1, "%Y-%m-%d")))
timestamp_day2 = int(time.mktime(time.strptime(day2, "%Y-%m-%d")))
result = int(format((timestamp_day1 - timestamp_day2) // 60 // 60 // 24))
number = int(result / 7)
time.sleep(10)
class 舆情预警(unittest.TestCase):
    def 打开舆情预警页面(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[2]/a').click()
        time.sleep(5)
        a = dr.find_element_by_class_name('switch-inner').text
        time.sleep(3)
        if (a == "开启"):
            pass
        else:
            raise EnvironmentError("打开舆情预警页面失败")

    def 更改风险预警信息功能(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[1]/ul/li[2]/div[2]/span[2]/span').click()
        time.sleep(1)
        chick_a = dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/ul/li[2]/div[2]/span[2]/span').get_attribute('class')
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[1]/ul/li[3]/div[2]/span[2]/span').click()
        time.sleep(1)
        chick_b = dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/ul/li[3]/div[2]/span[2]/span').get_attribute('class')
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[1]/ul/li[3]/div[2]/span[2]/span').click()
        time.sleep(1)
        chick_c = dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/ul/li[3]/div[2]/span[2]/span').get_attribute('class')
        time.sleep(2)
        if (
                chick_a == 'iconfont icon-radio-checked' and chick_b == 'iconfont icon-radio-checked' and chick_c == 'iconfont icon-radio-checked'):
            a = 1
            pass
        else:
            raise EnvironmentError("更改风险预警信息功能异常")


    def 风险可视化关闭功能(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[1]/ul/li[3]/div[2]/span[2]/span').click()
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[1]/ul/li[3]/div[2]/span[7]/span').click()
        dr.find_element_by_class_name('switch-inner').click()
        time.sleep(2)
        a = dr.find_element_by_class_name('switch-inner').text
        if (a == "关闭"):
            pass
        else:
            raise EnvironmentError("风险可视化关闭功能异常")

    def 最新国别风险报告弹层(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[2]/div/a[2]/span[1]').click()
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div/div[1]/div[2]/div').click()
        time.sleep(3)
        gbfx = dr.find_element_by_class_name('modal-title').text
        if (gbfx == "最新国别风险"):
            pass
        else:
            raise EnvironmentError("最新国别风险弹层显示异常")

    def 国别风险pdf显示(self):
        a = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if(re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/div/span[2]').get_attribute('class')
            re_2 = re.findall(".*confont (.*).*", b)
            if(re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[3]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        if (re_one[0] == "2F61f6e72c-c02d-11ea-b1b8-1a5b4e4f5a6a" and re_tow[
            0] == "2Fe5071022-bde6-11ea-a2f0-1a5b4e4f5a6a" and re_three[0] == "2F7df65d2c-c02d-11ea-ab2d-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("国别风险pdf显示异常")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

    def 最新舆情信息弹层(self):
        time.sleep(2)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[2]/div/a[2]/span[1]').click()
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div/div[2]/div[2]/div').click()
        time.sleep(3)
        yqxx = dr.find_element_by_class_name('modal-title').text
        if (yqxx == "最新舆情信息"):
            pass
        else:
            raise EnvironmentError("最新舆情信息弹层显示异常")

    def 舆情信息模块功能(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/table/tbody/tr[2]/td[1]/div').click()
        time.sleep(1)
        yqxx_a_l = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/table/tbody/tr[2]/td[1]/div').text
        yqxx_a_r = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div').text
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/table/tbody/tr[4]/td[1]/div').click()
        yqxx_b_l = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/table/tbody/tr[4]/td[1]/div').text
        yqxx_b_r = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div').text
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/table/tbody/tr[6]/td[1]/div').click()
        yqxx_c_l = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[1]/table/tbody/tr[6]/td[1]/div').text
        yqxx_c_r = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div[2]/div[2]/div[3]/div[2]/div').text
        time.sleep(3)
        if (yqxx_a_l == yqxx_a_r and yqxx_b_l == yqxx_b_r and yqxx_c_l == yqxx_c_r):
            pass
        else:
            raise EnvironmentError("最新舆情信息模块异常")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

    def 最新安全周报弹层(self):
        time.sleep(2)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[2]/div/a[2]/span[1]').click()
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div/div[3]/div[2]/div').click()
        time.sleep(3)
        aqzb = dr.find_element_by_class_name('modal-title').text
        if (aqzb == "最新安全周报"):
            pass
        else:
            raise EnvironmentError("最新安全周报弹层显示异常")

    def 安全周报模块功能(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td/div').click()
        time.sleep(1)
        aqzb_a_l = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[2]/td/div').text
        aqzb_a_r = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/div[2]/h2').text
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[8]/td/div').click()
        aqzb_b_l = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[8]/td/div').text
        aqzb_b_r = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/div[2]/h2').text
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[17]/td/div').click()
        aqzb_c_l = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[17]/td/div').text
        aqzb_c_r = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/div[2]/h2').text
        time.sleep(3)
        if (aqzb_a_l == aqzb_a_r and aqzb_b_l == aqzb_b_r and aqzb_c_l == aqzb_c_r):
            pass
        else:
            raise EnvironmentError("最新安全周报模块异常")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

    def 最新预警信息弹层(self):
        time.sleep(2)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[2]/div/a[2]/span[1]').click()
        time.sleep(5)
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div/div[4]/div[2]/div').click()
        time.sleep(3)
        yjxx = dr.find_element_by_class_name('modal-title').text
        if (yjxx == "最新预警消息"):
            pass
        else:
            raise EnvironmentError("最新预警信息弹层显示异常")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

    def 安全周报最新期数(self):
        time.sleep(2)
        weekly_no = int(request_test.shandong_week_no())
        if (number <= weekly_no):
            pass
        else:
            raise EnvironmentError("安全周报最新期数显示期数异常")


class 一带一路舆情预警(unittest.TestCase):
    def 国别风险pdf显示(self):
        a = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if(re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute('class')
            re_2 = re.findall(".*confont (.*).*", b)
            if(re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        if (re_one[0] == "2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a" and re_tow[
            0] == "2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a" and re_three[0] == "2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("国别风险pdf显示异常")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

    def 安全周报最新期数(self):
        time.sleep(2)
        weekly_no = int(request_test.B_and_r_week_no())
        if (number <= weekly_no):
            pass
        else:
            raise EnvironmentError("安全周报最新期数显示期数异常")

class 北方工业舆情预警(unittest.TestCase):
    def 国别风险pdf显示(self):
        a = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if(re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute('class')
            re_2 = re.findall(".*confont (.*).*", b)
            if(re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

        if (re_one[0] == "2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a" and re_tow[
            0] == "2F7df65d2c-c02d-11ea-ab2d-1a5b4e4f5a6a" and re_three[0] == "2Fdae48368-bde6-11ea-9a8a-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("国别风险pdf显示异常")

    def 安全周报最新期数(self):
        time.sleep(2)
        weekly_no = int(request_test.N_Industrial_week_no())
        if (number <= weekly_no):
            pass
        else:
            raise EnvironmentError("安全周报最新期数显示期数异常")

class 中交集团舆情信息(unittest.TestCase):
    def 国别风险pdf显示(self):
        a = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if(re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute('class')
            re_2 = re.findall(".*confont (.*).*", b)
            if(re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[5]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

        if (re_one[0] == "2Ff6a9cfc4-c02d-11ea-843c-1a5b4e4f5a6a" and re_tow[
            0] == "2Fe7fa2a9e-bde6-11ea-b2a6-1a5b4e4f5a6a" and re_three[0] == "2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("国别风险pdf显示异常")

    def 安全周报最新期数(self):
        time.sleep(2)
        weekly_no = int(request_test.China_Traffic_week_no())
        if (number <= weekly_no):
            pass
        else:
            raise EnvironmentError("安全周报最新期数显示期数异常")

class 鼎昊国际舆情信息(unittest.TestCase):
    def 国别风险pdf显示(self):
        a = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if(re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute('class')
            re_2 = re.findall(".*confont (.*).*", b)
            if(re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fe686b25e-bde6-11ea-a3a6-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Ff1ffd1ec-bde6-11ea-84e7-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)

        a = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').get_attribute('class')
        re_1 = re.findall(".*confont (.*).*", a)
        if (re_1[0] == 'icon-plus'):
            dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
            time.sleep(2)
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                #'2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        else:
            b = dr.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').get_attribute(
                'class')
            re_2 = re.findall(".*confont (.*).*", b)
            if (re_2[0] == 'icon-plus'):
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
                time.sleep(2)
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
                # '2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a'
            else:
                dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li/div/a').click()
                time.sleep(3)
                pdf_url = dr.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
                re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()

        if (re_one[0] == "2Ff5b8990e-bde6-11ea-88b9-1a5b4e4f5a6a" and re_tow[
            0] == "2Fe7fa2a9e-bde6-11ea-b2a6-1a5b4e4f5a6a" and re_three[0] == "2Fde8762b0-bde6-11ea-abc9-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("国别风险pdf显示异常")

    def 安全周报最新期数(self):
        time.sleep(2)
        weekly_no = int(request_test.T_Hrisk_week_no())
        if (number <= weekly_no):
            pass
        else:
            raise EnvironmentError("安全周报最新期数显示期数异常")