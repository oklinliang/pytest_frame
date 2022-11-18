import time
import unittest
import request_test
import driver

zbjgzs = request_test.zbjgzs()
qyxmzs = request_test.qyjgzs()
jgzrs = request_test.jgzrs()
B_and_r_zbjgzs = request_test.B_and_r_zbjgzs()
N_Industrial_zbjgzs = request_test.N_Industrial_zbjgzs()
China_Traffic_zbjgzs = request_test.China_Traffic_zbjgzs()
T_Hrisk_zbjgzs = request_test.T_Hrisk_zbjgzs()
T_Hrisk_jgzrs = request_test.T_Hrisk_jgzrs()
xyqz_requ = int(request_test.xyqz())
ljqz_requ = int(request_test.ljqz())
xyzy_requ = int(request_test.xyzy())
xysw_requ = int(request_test.xysw())

time.sleep(10)
dr = driver.dr
class 疫情管理(unittest.TestCase):
    def 打开疫情管理页面(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[3]/a').click()
        time.sleep(10)
        index_test = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[1]/div[1]/span').text
        if(index_test == "疫情地图"):
            pass
        else:
            raise EnvironmentError("疫情管理页面打开失败")

    def 驻外机构人数显示(self):
        zwjg = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[2]/span').text)
        if (zwjg == zbjgzs):
            pass
        else:
            raise EnvironmentError("驻外机构与项目管理处人数不一致")

    def 境外项目数显示(self):
        jwxms = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[3]/span').text)
        if (jwxms == qyxmzs):
            pass
        else:
            raise EnvironmentError("境外与项目管理处人数不一致")

    def 中方员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[5]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[3]').text)
        if (zfrs == zfrsjz):
            pass
        else:
            raise EnvironmentError("中方人数两处显示不一致")

    def 外方员工人数显示(self):
        wfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        wfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        if (wfrs == wfrsjz):
            pass
        else:
            raise EnvironmentError("外方人数两处显示不一致")

    def 总员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[5]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[3]').text)
        wfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        wfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        if (zfrs == zfrsjz and wfrs == wfrsjz):
            zrs = zfrs + wfrs
            if (zrs == jgzrs):
                pass
            else:
                raise EnvironmentError("总人数显示异常")

    def 海外疫情动态显示(self):
        time.sleep(3)
        xyqz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/div[1]/div[2]/div[1]/div[7]/div/div/div[1]/span[1]').text)
        ljqz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/div[1]/div[2]/div[1]/div[7]/div/div/div[2]/span[1]').text)
        xyzy = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/div[1]/div[2]/div[1]/div[7]/div/div/div[3]/span[1]').text)
        xysw = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[1]/div[1]/div[2]/div[1]/div[7]/div/div/div[4]/span[1]').text)
        if (xysw == xysw_requ and xyqz == xyqz_requ and ljqz == ljqz_requ and xyzy == xyzy_requ):
            pass
        else:
            raise EnvironmentError("海外疫情动态处显示异常")

    def 境外人员情况弹层显示(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[3]/div[1]/div[1]/span[2]/i').click()
        time.sleep(3)
        bt = dr.find_element_by_id("rcDialogTitle0").text
        if (bt == "境外人员情况"):
            pass
        else:
            raise EnvironmentError("境外人员情况弹层显示异常")

    def 境外人员情况弹层每日汇总表展示(self):
        day_text = dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/section/section/main/div/div/div/div/div/div/div[1]/table/thead/tr[1]/th[1]').text
        if (day_text == '洲别'):
            pass
        else:
            raise EnvironmentError("境外人员情况弹层每日汇总表展示异常")

    def 境外人员情况弹层周变化表展示(self):
        dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/section/header/div/span[2]/a').click()
        time.sleep(2)
        week_text = dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/section/section/main/div/div/div/div/div/div/div[1]/table/thead/tr[1]/th[1]').text
        if (week_text == '洲别'):
            pass
        else:
            raise EnvironmentError("境外人员情况弹层周变化表展示异常")
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/button/span/span').click()
        time.sleep(2)

    def 疫情防控日报弹层展示(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[3]/div[2]/div[1]/span[2]/i').click()
        time.sleep(3)
        bt = dr.find_element_by_id("rcDialogTitle1").text
        if (bt == "疫情防控日报"):
            pass
        else:
            raise EnvironmentError("疫情防控日报弹层展示异常")

    def 疫情防控日报弹层列表显示(self):
        day_text = dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/table/thead/tr[1]/th[1]').text
        if (day_text == "权属单位"):
            pass
        else:
            raise EnvironmentError("疫情防控日报弹层列表显示异常")
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/button/span/span').click()

class 一带一路疫情管理(unittest.TestCase):
    def 承包项目数(self):
        zwjg = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[3]/span').text)
        if (zwjg == B_and_r_zbjgzs):
            pass
        else:
            raise EnvironmentError("承包项目数与项目管理处人数不一致")

    def 中方员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        if (zfrs == zfrsjz):
            pass
        else:
            raise EnvironmentError("中方人数两处显示不一致")

class 北方工业疫情管理(unittest.TestCase):
    def 承包项目数(self):
        zwjg = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[3]/span').text)
        if (zwjg == N_Industrial_zbjgzs):
            pass
        else:
            raise EnvironmentError("承包项目数与项目管理处人数不一致")

    def 中方员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        if (zfrs == zfrsjz):
            pass
        else:
            raise EnvironmentError("中方人数两处显示不一致")

class 中交集团疫情管理(unittest.TestCase):
    def 承包项目数(self):
        zwjg = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[3]/span').text)
        if (zwjg == China_Traffic_zbjgzs):
            pass
        else:
            raise EnvironmentError("承包项目数与项目管理处人数不一致")

    def 中方员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        if (zfrs == zfrsjz):
            pass
        else:
            raise EnvironmentError("中方人数两处显示不一致")

class 鼎昊国际疫情管理(unittest.TestCase):
    def 承包项目数(self):
        zwjg = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[3]/span').text)
        if (zwjg == T_Hrisk_zbjgzs):
            pass
        else:
            raise EnvironmentError("承包项目数与项目管理处人数不一致")

    def 中方员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        if (zfrs == zfrsjz):
            pass
        else:
            raise EnvironmentError("中方人数两处显示不一致")

    def 外方员工人数显示(self):
        wfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[7]/span').text)
        wfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[5]').text)
        if (wfrs == wfrsjz):
            pass
        else:
            raise EnvironmentError("外方人数两处显示不一致")

    def 总员工人数显示(self):
        zfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[6]/span').text)
        zfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[4]').text)
        wfrs = int(dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div/div[7]/span').text)
        wfrsjz = int(dr.find_element_by_xpath(
            '//*[@id="authViewer"]/div/div/div[3]/div[1]/div[2]/div[1]/div[7]/div/div/div/div/div/div[2]/span[5]').text)
        if (zfrs == zfrsjz and wfrs == wfrsjz):
            zrs = zfrs + wfrs
            if (zrs == T_Hrisk_jgzrs):
                pass
            else:
                raise EnvironmentError("总人数显示异常")