import time
import re
import unittest
import driver
import request_test
from selenium.webdriver.common.keys import Keys

jgrs = str(request_test.jgrs())
other_rs = request_test.other_rs()
other_jgzs = request_test.other_jgzs()
China_Traffic_jgrs = str(request_test.China_Traffic_jgrs())
China_Traffic_other_rs = request_test.China_Traffic_other_rs()
China_Traffic_other_jgzs = request_test.China_Traffic_other_jgzs()
T_Hrisk_jgrs = str(request_test.T_Hrisk_jgrs())
T_Hrisk_other_rs = request_test.T_Hrisk_other_rs()
T_Hrisk_other_jgzs = request_test.T_Hrisk_other_jgzs()

dr = driver.dr
time.sleep(10)
class 项目管理(unittest.TestCase):
    def 打开项目管理页面(self):
        time.sleep(20)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[1]/a/span').click()
        # 由于地图原因相应时间有些长，等待20秒响应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("打开项目管理页面失败")



    def 法律法规(self):
        dr.find_elements_by_class_name('btn-item-list')[0].click()
        time.sleep(1)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "法律法规"):
            pass
        else:
            raise EnvironmentError("打开法律法规弹层失败")

    def 法律法规_亚洲pdf校验(self):
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[2]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2Fd3ebdc52-c00a-11ea-b5b7-1a5b4e4f5a6a" and re_other[
            0] == "2Fdaf52990-c00a-11ea-b0ea-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("亚洲显示异常")

    def 法律法规_欧洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[3]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[3]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[3]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[3]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[3]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2F9b2e54a6-c00c-11ea-93f0-1a5b4e4f5a6a" and re_other[
            0] == "2F9fa327f0-c00c-11ea-a1ff-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("欧洲显示异常")

    def 法律法规_非洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2Fc914f1b8-c00c-11ea-9508-1a5b4e4f5a6a" and re_other[
            0] == "2Fcfcf07a0-c00c-11ea-bd6b-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("非洲显示异常")

    def 法律法规_南美洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_jiben[0] == "2F3d481dc0-c00e-11ea-a6f3-1a5b4e4f5a6a" and re_other[
            0] == "2F528a69a4-c00e-11ea-a037-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("南美洲显示异常")

    def 预案管理(self):
        dr.find_elements_by_class_name('btn-item-list')[1].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "预案管理"):
            pass
        else:
            raise EnvironmentError("打开预案管理弹层失败")

    def 预案管理pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[2]/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li[7]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_one[0] == "2F723f4e96-c0f3-11ea-b85b-1a5b4e4f5a6a" and re_tow[
            0] == "2Fe9fc9dc0-c0fe-11ea-b3dd-1a5b4e4f5a6a" and re_three[0] == "2Fnone"):
            pass
        else:
            raise EnvironmentError("预案管理pdf显示异常")

    def 文件管理(self):
        dr.find_elements_by_class_name('btn-item-list')[2].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "文件管理"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度(self):
        dr.find_elements_by_class_name('btn-item-list')[3].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "规章制度"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[1]/ul/li[3]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_one[0] == "2Fabbe6b7a-c102-11ea-af63-1a5b4e4f5a6a" and re_tow[
            0] == "2Ff16de206-c105-11ea-a230-1a5b4e4f5a6a" and re_three[0] == "2Facb853fc-c106-11ea-a9e3-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("规章制度pdf显示异常")

    def 培训台账(self):
        dr.find_elements_by_class_name('btn-item-list')[4].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训台账"):
            pass
        else:
            raise EnvironmentError("打开培训台账弹层失败")

    def 体检报告(self):
        dr.find_elements_by_class_name('btn-item-list')[5].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "体检报告"):
            pass
        else:
            raise EnvironmentError("打开体检报告弹层失败")

    def 保险记录(self):
        dr.find_elements_by_class_name('btn-item-list')[6].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "保险记录"):
            pass
        else:
            raise EnvironmentError("打开保险记录弹层失败")

    def 评估报告(self):
        dr.find_elements_by_class_name('btn-item-list')[7].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "评估报告"):
            pass
        else:
            raise EnvironmentError("打开评估报告弹层失败")

    def 现场医疗(self):
        dr.find_elements_by_class_name('btn-item-list')[8].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "现场医疗"):
            pass
        else:
            raise EnvironmentError("打开现场医疗弹层失败")

    def 培训演练(self):
        dr.find_elements_by_class_name('btn-item-list')[9].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训演练"):
            pass
        else:
            raise EnvironmentError("打开培训演练弹层失败")

    def 安保方案(self):
        dr.find_elements_by_class_name('btn-item-list')[10].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "安保方案"):
            pass
        else:
            raise EnvironmentError("打开安保方案弹层失败")

    def 医疗转运(self):
        dr.find_elements_by_class_name('btn-item-list')[11].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "医疗转运"):
            pass
        else:
            raise EnvironmentError("打开医疗转运弹层失败")

    def 机构人数校验(self):
        time.sleep(2)
        popno_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        popno_b = re.findall(".*人数（(.*)\）.*", popno_a)
        popno_zong = int(popno_b[0])
        zzpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/span').text)
        pqpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/span').text)
        fbpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[3]/span').text)
        yjpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[4]/span').text)
        pattern = re.compile(r"'value': (.*?)\}")
        result = pattern.findall(jgrs)
        requ_jgrs = int(result[0]) + int(result[1]) + int(result[2]) + int(result[3])
        ui_rs = zzpop + pqpop + fbpop + yjpop
        if(popno_zong == requ_jgrs == ui_rs):
            pass
        else:
            raise EnvironmentError("机构总人数显示异常")

    def 选择其他机构进行人数校验(self):
        time.sleep(2)
        dr.find_element_by_id('rc_select_2').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_2').send_keys(Keys.DOWN)
        time.sleep(1)
        dr.find_element_by_id('rc_select_2').send_keys(Keys.ENTER)
        time.sleep(2)
        dr.find_element_by_id('rc_select_3').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_3').send_keys(Keys.ENTER)
        time.sleep(3)
        pop_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        pop_b = int(re.findall(".*人数（(.*)\）.*", pop_a)[0])
        if(pop_b != 0):
            other_ui_rs = other_rs[0] + other_rs[1] + other_rs[2] + other_rs[3]
            if(other_ui_rs == pop_b):
                pass
            else:
                raise EnvironmentError("其他机构人数显示异常")

    def 在某机构公司下的机构人数(self):
        time.sleep(2)
        my_text_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        my_text_b = int(re.findall(".*人数（(.*)\）.*", my_text_a)[0])
        a = other_jgzs
        b = len(a)
        c = []
        d = 0
        for i in range(b):
            c.append(int(a[i]))
        for i in range(b):
            d = d + c[i]
        if(my_text_b == d):
            pass
        else:
            raise EnvironmentError("在某机构公司下的机构人数显示异常")

class 一带一路项目管理(unittest.TestCase):
    def 打开项目管理页面(self):
        time.sleep(10)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[1]/a/span').click()
        # 由于地图原因相应时间有些长，等待20秒响应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "港口信息"):
            pass
        else:
            raise EnvironmentError("登录失败")

    def 港口介绍(self):
        dr.find_elements_by_class_name('btn-item-list')[0].click()
        time.sleep(1)
        code_text = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/iframe').get_attribute('src')
        code_text = re.findall(".*beijing.aliyuncs.com/(.*).pdf.*", code_text)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        if (code_text[0] == "GwadarPort"):
            pass
        else:
            raise EnvironmentError("打开港口介绍弹层失败")


    def 历史图像(self):
        dr.find_elements_by_class_name('btn-item-list')[1].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "历史图像"):
            pass
        else:
            raise EnvironmentError("打开历史图像弹层失败")

    def 港口航线(self):
        dr.find_elements_by_class_name('btn-item-list')[2].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "港口航线"):
            pass
        else:
            raise EnvironmentError("打开港口航线弹层失败")

    def 当地法律(self):
        dr.find_elements_by_class_name('btn-item-list')[3].click()
        time.sleep(1)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "法律法规"):
            pass
        else:
            raise EnvironmentError("打开法律法规弹层失败")

    def 当地法律_亚洲pdf校验(self):
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2F0f68fcf4-d2f0-11ea-9422-1a5b4e4f5a6a" and re_other[
            0] == "2F164ba094-d2f0-11ea-9fb2-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("亚洲显示异常")

    def 当地法律_非洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2Fd639e29a-d2ef-11ea-949a-1a5b4e4f5a6a" and re_other[
            0] == "2Feea14382-d2ef-11ea-b918-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("非洲显示异常")

    def 当地法律_南美洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_jiben[0] == "2Fecc01cb0-fe36-11ea-b6a9-0242ac120002" and re_other[
            0] == "2Ffda5b1de-fe36-11ea-b536-0242ac120002"):
            pass
        else:
            raise EnvironmentError("南美洲显示异常")

    def 运载信息(self):
        dr.find_elements_by_class_name('btn-item-list')[4].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "运载信息"):
            pass
        else:
            raise EnvironmentError("打开运载信息弹层失败")

    def 评估报告(self):
        dr.find_elements_by_class_name('btn-item-list')[5].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "评估报告"):
            pass
        else:
            raise EnvironmentError("打开评估报告弹层失败")

class 北方工业项目管理(unittest.TestCase):
    def 打开项目管理页面(self):
        time.sleep(20)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[1]/a/span').click()
        # 由于地图原因相应时间有些长，等待20秒响应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("打开项目管理页面失败")

    def 法律法规(self):
        dr.find_elements_by_class_name('btn-item-list')[0].click()
        time.sleep(1)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "法律法规"):
            pass
        else:
            raise EnvironmentError("打开法律法规弹层失败")

    def 法律法规_亚洲pdf校验(self):
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        #'2F0f68fcf4-d2f0-11ea-9422-1a5b4e4f5a6a'
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        #'2F164ba094-d2f0-11ea-9fb2-1a5b4e4f5a6a'
        time.sleep(1)
        if (re_jiben[0] == "2F0f68fcf4-d2f0-11ea-9422-1a5b4e4f5a6a" and re_other[
            0] == "2F164ba094-d2f0-11ea-9fb2-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("亚洲显示异常")

    def 法律法规_非洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        #'2Fc914f1b8-c00c-11ea-9508-1a5b4e4f5a6a'
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        #'2Fcfcf07a0-c00c-11ea-bd6b-1a5b4e4f5a6a'
        time.sleep(1)
        if (re_jiben[0] == "2Fc914f1b8-c00c-11ea-9508-1a5b4e4f5a6a" and re_other[
            0] == "2Fcfcf07a0-c00c-11ea-bd6b-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("非洲显示异常")

    def 法律法规_南美洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        #'2F3d481dc0-c00e-11ea-a6f3-1a5b4e4f5a6a'
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        #'2F528a69a4-c00e-11ea-a037-1a5b4e4f5a6a'
        time.sleep(1)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_jiben[0] == "2F3d481dc0-c00e-11ea-a6f3-1a5b4e4f5a6a" and re_other[
            0] == "2F528a69a4-c00e-11ea-a037-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("南美洲显示异常")

    def 预案管理(self):
        dr.find_elements_by_class_name('btn-item-list')[1].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        if (code_text == "预案管理"):
            pass
        else:
            raise EnvironmentError("打开预案管理弹层失败")

    def 文件管理(self):
        dr.find_elements_by_class_name('btn-item-list')[2].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "文件管理"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度(self):
        dr.find_elements_by_class_name('btn-item-list')[3].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        if (code_text == "规章制度"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 培训台账(self):
        dr.find_elements_by_class_name('btn-item-list')[4].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训台账"):
            pass
        else:
            raise EnvironmentError("打开培训台账弹层失败")

    def 体检报告(self):
        dr.find_elements_by_class_name('btn-item-list')[5].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "体检报告"):
            pass
        else:
            raise EnvironmentError("打开体检报告弹层失败")

    def 保险记录(self):
        dr.find_elements_by_class_name('btn-item-list')[6].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "保险记录"):
            pass
        else:
            raise EnvironmentError("打开保险记录弹层失败")

    def 评估报告(self):
        dr.find_elements_by_class_name('btn-item-list')[7].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "评估报告"):
            pass
        else:
            raise EnvironmentError("打开评估报告弹层失败")

    def 现场医疗(self):
        dr.find_elements_by_class_name('btn-item-list')[8].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "现场医疗"):
            pass
        else:
            raise EnvironmentError("打开现场医疗弹层失败")

    def 培训演练(self):
        dr.find_elements_by_class_name('btn-item-list')[9].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训演练"):
            pass
        else:
            raise EnvironmentError("打开培训演练弹层失败")

    def 安保方案(self):
        dr.find_elements_by_class_name('btn-item-list')[10].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "安保方案"):
            pass
        else:
            raise EnvironmentError("打开安保方案弹层失败")

    def 医疗转运(self):
        dr.find_elements_by_class_name('btn-item-list')[11].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "医疗转运"):
            pass
        else:
            raise EnvironmentError("打开医疗转运弹层失败")

class 中交集团项目管理(unittest.TestCase):
    def 打开项目管理页面(self):
        time.sleep(20)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[1]/a/span').click()
        # 由于地图原因相应时间有些长，等待20秒响应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("打开项目管理页面失败")

    def 法律法规(self):
        dr.find_elements_by_class_name('btn-item-list')[0].click()
        time.sleep(1)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "法律法规"):
            pass
        else:
            raise EnvironmentError("打开法律法规弹层失败")

    def 法律法规_亚洲pdf校验(self):
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2Fea7c64b0-d882-11ea-ae14-1a5b4e4f5a6a" and re_other[
            0] == "2Ff92aba7a-d882-11ea-97b0-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("亚洲显示异常")

    def 法律法规_欧洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[5]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[5]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[5]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[5]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[5]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2F310a6f9e-d2f2-11ea-96d2-1a5b4e4f5a6a" and re_other[
            0] == "2F35dca06e-d2f2-11ea-a68f-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("欧洲显示异常")

    def 法律法规_非洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2Fd639e29a-d2ef-11ea-949a-1a5b4e4f5a6a" and re_other[
            0] == "2Feea14382-d2ef-11ea-b918-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("非洲显示异常")

    def 法律法规_南美洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[1]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[2]/div/span[2]').click()
        time.sleep(1)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_jiben[0] == "2Fecc01cb0-fe36-11ea-b6a9-0242ac120002" and re_other[
            0] == "2Ffda5b1de-fe36-11ea-b536-0242ac120002"):
            pass
        else:
            raise EnvironmentError("南美洲显示异常")

    def 预案管理(self):
        dr.find_elements_by_class_name('btn-item-list')[1].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "预案管理"):
            pass
        else:
            raise EnvironmentError("打开预案管理弹层失败")

    def 预案管理pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[1]/ul/li[3]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_one[0] == "2F8iFMlbf9LnkT4mn3Kctrdw-kP2f44AA3" and re_tow[
            0] == "2Fnone" and re_three[0] == "2F91fcb170-e6b8-11ea-860c-0242f326aa85"):
            pass
        else:
            raise EnvironmentError("预案管理pdf显示异常")

    def 文件管理(self):
        dr.find_elements_by_class_name('btn-item-list')[2].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "文件管理"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度(self):
        dr.find_elements_by_class_name('btn-item-list')[3].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "规章制度"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[2]/ul/li[25]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_one[0] == "2F5f89d548-ae0e-11ea-83e3-02426dc8d3df" and re_tow[
            0] == "2F25bf7662-aebb-11ea-8bf4-02426dc8d3df" and re_three[0] == "2Fnone"):
            pass
        else:
            raise EnvironmentError("规章制度pdf显示异常")

    def 培训台账(self):
        dr.find_elements_by_class_name('btn-item-list')[4].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训台账"):
            pass
        else:
            raise EnvironmentError("打开培训台账弹层失败")

    def 体检报告(self):
        dr.find_elements_by_class_name('btn-item-list')[5].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "体检报告"):
            pass
        else:
            raise EnvironmentError("打开体检报告弹层失败")

    def 保险记录(self):
        dr.find_elements_by_class_name('btn-item-list')[6].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "保险记录"):
            pass
        else:
            raise EnvironmentError("打开保险记录弹层失败")

    def 评估报告(self):
        dr.find_elements_by_class_name('btn-item-list')[7].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "评估报告"):
            pass
        else:
            raise EnvironmentError("打开评估报告弹层失败")

    def 现场医疗(self):
        dr.find_elements_by_class_name('btn-item-list')[8].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "现场医疗"):
            pass
        else:
            raise EnvironmentError("打开现场医疗弹层失败")

    def 培训演练(self):
        dr.find_elements_by_class_name('btn-item-list')[9].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训演练"):
            pass
        else:
            raise EnvironmentError("打开培训演练弹层失败")

    def 安保方案(self):
        dr.find_elements_by_class_name('btn-item-list')[10].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "安保方案"):
            pass
        else:
            raise EnvironmentError("打开安保方案弹层失败")

    def 医疗转运(self):
        dr.find_elements_by_class_name('btn-item-list')[11].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "医疗转运"):
            pass
        else:
            raise EnvironmentError("打开医疗转运弹层失败")

    def 机构人数校验(self):
        time.sleep(2)
        popno_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        popno_b = re.findall(".*人数（(.*)\）.*", popno_a)
        popno_zong = int(popno_b[0])
        zzpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/span').text)
        pqpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/span').text)
        fbpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[3]/span').text)
        yjpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[4]/span').text)
        pattern = re.compile(r"'value': '(.*?)', 'name'*")
        result = pattern.findall(China_Traffic_jgrs)
        b = len(result)
        requ_jgrs = 0
        for i in range(b):
            requ_jgrs += int(result[i])
        ui_rs = zzpop + pqpop + fbpop + yjpop
        if(popno_zong == requ_jgrs == ui_rs):
            pass
        else:
            raise EnvironmentError("机构总人数显示异常")

    def 选择其他机构进行人数校验(self):
        time.sleep(2)
        dr.find_element_by_id('rc_select_2').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_2').send_keys(Keys.DOWN)
        time.sleep(1)
        dr.find_element_by_id('rc_select_2').send_keys(Keys.ENTER)
        time.sleep(2)
        dr.find_element_by_id('rc_select_3').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_3').send_keys(Keys.ENTER)
        time.sleep(2)
        dr.find_element_by_id('rc_select_4').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_4').send_keys(Keys.ENTER)
        time.sleep(3)
        pop_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        pop_b = int(re.findall(".*人数（(.*)\）.*", pop_a)[0])
        if(pop_b != 0):
            c = len(China_Traffic_other_rs)
            other_ui_rs = 0
            for i in range(c):
                other_ui_rs += int(China_Traffic_other_rs[i])
            if(other_ui_rs == pop_b):
                pass
            else:
                raise EnvironmentError("其他机构人数显示异常")

    def 在某机构公司下的机构总数(self):
        time.sleep(2)
        my_text_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        my_text_b = int(re.findall(".*人数（(.*)\）.*", my_text_a)[0])
        a = China_Traffic_other_jgzs
        b = len(a)
        c = []
        d = 0
        for i in range(b):
            c.append(int(a[i]))
        for i in range(b):
            d = d + c[i]
        if(my_text_b == d):
            pass
        else:
            raise EnvironmentError("在某机构公司下的机构总数显示异常")

class 鼎昊国际项目管理(unittest.TestCase):
    def 打开项目管理页面(self):
        time.sleep(20)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[1]/a/span').click()
        # 由于地图原因相应时间有些长，等待20秒响应
        time.sleep(20)
        code_text = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/span').text
        if (code_text == "项目管理"):
            pass
        else:
            raise EnvironmentError("打开项目管理页面失败")

    def 法律法规(self):
        dr.find_elements_by_class_name('btn-item-list')[0].click()
        time.sleep(1)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "法律法规"):
            pass
        else:
            raise EnvironmentError("打开法律法规弹层失败")

    def 法律法规_亚洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[3]/ul/li[1]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(1)
        if (re_jiben[0] == "2F12550198-d2ef-11ea-93f2-1a5b4e4f5a6a" and re_other[
            0] == "2F1790ec6c-d2ef-11ea-9240-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("亚洲显示异常")

    def 法律法规_欧洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[3]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[3]/ul/li[1]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[3]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[3]/ul/li[2]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[4]/ul/li[3]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(5)
        if (re_jiben[0] == "2F1748a216-d2ec-11ea-84bb-1a5b4e4f5a6a" and re_other[
            0] == "2F1db8e89a-d2ec-11ea-a7c7-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("欧洲显示异常")

    def 法律法规_非洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[7]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[7]/ul/li[1]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[7]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[7]/ul/li[2]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[5]/ul/li[7]/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(5)
        if (re_jiben[0] == "2Fc206d52e-d2f1-11ea-b641-1a5b4e4f5a6a" and re_other[
            0] == "2Fc7e74f3c-d2f1-11ea-8030-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("非洲显示异常")

    def 法律法规_南美洲pdf校验(self):
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[1]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[1]/ul/li/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_jiben = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[2]/div/span[2]').click()
        time.sleep(5)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li[6]/ul/li[2]/ul/li[2]/ul/li[2]/div/a').click()
        time.sleep(2)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute('src')
        re_other = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(5)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(5)
        if (re_jiben[0] == "2F3d481dc0-c00e-11ea-a6f3-1a5b4e4f5a6a" and re_other[
            0] == "2F5632a738-c00e-11ea-a131-1a5b4e4f5a6a"):
            pass
        else:
            raise EnvironmentError("南美洲显示异常")

    def 预案管理(self):
        dr.find_elements_by_class_name('btn-item-list')[1].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "预案管理"):
            pass
        else:
            raise EnvironmentError("打开预案管理弹层失败")

    def 预案管理pdf校验(self):
        time.sleep(10)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[1]/ul/li[4]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_one[0] == "2F20ad3e0e-e6b8-11ea-81ce-0242f326aa85" and re_tow[
            0] == "2Fnone"):
            pass
        else:
            raise EnvironmentError("预案管理pdf显示异常")

    def 文件管理(self):
        dr.find_elements_by_class_name('btn-item-list')[2].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "文件管理"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度(self):
        dr.find_elements_by_class_name('btn-item-list')[3].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        if (code_text == "规章制度"):
            pass
        else:
            raise EnvironmentError("打开文件管理弹层失败")

    def 规章制度pdf校验(self):
        time.sleep(10)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[1]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_one = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[2]/ul/li[1]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_tow = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[1]/div/ul/li/ul/li[2]/ul/li[25]/div/a').click()
        time.sleep(3)
        pdf_url = dr.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div/div[4]/div/div[2]/iframe').get_attribute(
            'src')
        re_three = re.findall(".*aliyuncs.com%(.*).pdf.*", pdf_url)
        time.sleep(2)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(1)
        if (re_one[0] == "2F5f89d548-ae0e-11ea-83e3-02426dc8d3df" and re_tow[
            0] == "2F25bf7662-aebb-11ea-8bf4-02426dc8d3df" and re_three[0] == "2Fnone"):
            pass
        else:
            raise EnvironmentError("规章制度pdf显示异常")

    def 培训台账(self):
        dr.find_elements_by_class_name('btn-item-list')[4].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训台账"):
            pass
        else:
            raise EnvironmentError("打开培训台账弹层失败")

    def 体检报告(self):
        dr.find_elements_by_class_name('btn-item-list')[5].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "体检报告"):
            pass
        else:
            raise EnvironmentError("打开体检报告弹层失败")

    def 保险记录(self):
        dr.find_elements_by_class_name('btn-item-list')[6].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "保险记录"):
            pass
        else:
            raise EnvironmentError("打开保险记录弹层失败")

    def 评估报告(self):
        dr.find_elements_by_class_name('btn-item-list')[7].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "评估报告"):
            pass
        else:
            raise EnvironmentError("打开评估报告弹层失败")

    def 现场医疗(self):
        dr.find_elements_by_class_name('btn-item-list')[8].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "现场医疗"):
            pass
        else:
            raise EnvironmentError("打开现场医疗弹层失败")

    def 培训演练(self):
        dr.find_elements_by_class_name('btn-item-list')[9].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "培训演练"):
            pass
        else:
            raise EnvironmentError("打开培训演练弹层失败")

    def 安保方案(self):
        dr.find_elements_by_class_name('btn-item-list')[10].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "安保方案"):
            pass
        else:
            raise EnvironmentError("打开安保方案弹层失败")

    def 医疗转运(self):
        dr.find_elements_by_class_name('btn-item-list')[11].click()
        time.sleep(3)
        code_text = dr.find_element_by_class_name('modal-title').text
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)
        if (code_text == "医疗转运"):
            pass
        else:
            raise EnvironmentError("打开医疗转运弹层失败")

    def 机构人数校验(self):
        time.sleep(2)
        popno_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        popno_b = re.findall(".*人数（(.*)\）.*", popno_a)
        popno_zong = int(popno_b[0])
        zzpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[1]/span').text)
        pqpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[2]/span').text)
        fbpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[3]/span').text)
        yjpop = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[4]/span').text)
        pattern = re.compile(r"'value': '(.*?)', 'name'*")
        result = pattern.findall(T_Hrisk_jgrs)
        b = len(result)
        requ_jgrs = 0
        for i in range(b):
            requ_jgrs += int(result[i])
        ui_rs = zzpop + pqpop + fbpop + yjpop
        if(popno_zong == requ_jgrs == ui_rs):
            pass
        else:
            raise EnvironmentError("机构总人数显示异常")

    def 选择其他机构进行人数校验(self):
        time.sleep(2)
        dr.find_element_by_id('rc_select_2').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_2').send_keys(Keys.DOWN)
        time.sleep(1)
        dr.find_element_by_id('rc_select_2').send_keys(Keys.ENTER)
        time.sleep(2)
        dr.find_element_by_id('rc_select_3').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_3').send_keys(Keys.ENTER)
        time.sleep(2)
        dr.find_element_by_id('rc_select_4').click()
        time.sleep(1)
        dr.find_element_by_id('rc_select_4').send_keys(Keys.ENTER)
        time.sleep(3)
        pop_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        pop_b = int(re.findall(".*人数（(.*)\）.*", pop_a)[0])
        if(pop_b != 0):
            c = len(T_Hrisk_other_rs)
            other_ui_rs = 0
            for i in range(c):
                other_ui_rs += int(T_Hrisk_other_rs[i])
            if(other_ui_rs == pop_b):
                pass
            else:
                raise EnvironmentError("其他机构人数显示异常")

    def 在某机构公司下的机构总数(self):
        time.sleep(2)
        my_text_a = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[3]/div[1]/span').text
        my_text_b = int(re.findall(".*人数（(.*)\）.*", my_text_a)[0])
        a = T_Hrisk_other_jgzs
        b = len(a)
        c = []
        d = 0
        for i in range(b):
            c.append(int(a[i]))
        for i in range(b):
            d = d + c[i]
        if(my_text_b == d):
            pass
        else:
            raise EnvironmentError("在某机构公司下的机构总数显示异常")

