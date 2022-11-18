import time
import unittest
import driver

time.sleep(10)
dr = driver.dr
class 应急处置(unittest.TestCase):
    def 打开应急处置页面(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[4]/a').click()
        time.sleep(10)
        bjjl = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div[1]/div[1]/span').text
        sjsb = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div[2]/div[1]/span[1]').text
        yjsj = dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div[3]/div[1]/span').text
        if (bjjl == "报警记录" and sjsb == "事件上报" and yjsj == "正在处置的应急事件"):
            pass
        else:
            raise EnvironmentError("打开应急处置页面失败")

    def 打开事件上报弹层(self):
        dr.find_element_by_xpath('//*[@id="authViewer"]/div/div/div/div[2]/div[1]/span[2]').click()
        time.sleep(2)
        bt = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "事件上报"):
            pass
        else:
            raise EnvironmentError("事件上报弹层打开异常")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)

    def 打开应急事件弹层(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[4]/div/div[1]/span[1]').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "应急事件"):
            pass
        else:
            raise EnvironmentError("打开应急事件弹层失败")
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
        time.sleep(2)

    def 打开值班记录弹层(self):
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[4]/div/div[2]/span[1]').click()
        time.sleep(3)
        bt = dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "值班记录列表"):
            pass
        else:
            raise EnvironmentError("打开值班记录弹层失败")

    def 打开新增值班记录弹层(self):
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/button').click()
        time.sleep(2)
        bt = dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[3]/div/div[2]').text
        if (bt == "新增值班记录"):
            pass
        else:
            raise EnvironmentError("打开新增值班记录弹层失败")
        dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/button/span').click()
        time.sleep(1)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/button/span').click()
