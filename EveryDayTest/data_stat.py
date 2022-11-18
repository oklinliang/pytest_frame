import time
import unittest

import driver

time.sleep(10)
dr = driver.dr
class 数据统计(unittest.TestCase):
    def 打开数据统计页面(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[5]/a').click()
        time.sleep(10)
        index_test = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[1]/div[2]/div[1]').text
        if(index_test == "项目统计"):
            pass
        else:
            raise EnvironmentError("打开数据统计页面失败")

    def 打开数据统计旁的分析报告(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[1]/div[2]/div[2]/button').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "分析报告"):
            pass
        else:
            raise EnvironmentError("打开数据统计旁的分析报告失败")
        dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/button/span').click()
        time.sleep(1)

    def 打开项目管理统计旁的分析报告(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/button').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "分析报告"):
            pass
        else:
            raise EnvironmentError("打开数据统计旁的分析报告失败")
        dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/button/span').click()
        time.sleep(1)

    def 打开舆情预警统计旁的分析报告(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/button').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "分析报告"):
            pass
        else:
            raise EnvironmentError("打开数据统计旁的分析报告失败")
        dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/button/span').click()
        time.sleep(1)

    def 打开疫情管理统计旁的分析报告(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/button').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "分析报告"):
            pass
        else:
            raise EnvironmentError("打开数据统计旁的分析报告失败")
        dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/button/span').click()
        time.sleep(1)

    def 打开应急处置统计旁的分析报告(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/button').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "分析报告"):
            pass
        else:
            raise EnvironmentError("打开数据统计旁的分析报告失败")
        dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/button/span').click()
        time.sleep(1)


