import time
import unittest
import driver

time.sleep(10)
dr = driver.dr
class 登出(unittest.TestCase):
    def 登出当前账号(self):
        time.sleep(3)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[2]/ul/li[1]/a').click()
        time.sleep(30)
        dr.find_element_by_xpath('//*[@id="appViewer"]/div[1]/div[2]/span[2]/span/span/span[2]').click()
        time.sleep(3)
        dr.find_element_by_xpath('/html/body/div[3]/div/ul/li[3]').click()
        time.sleep(3)
        dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div/button[1]').click()
        index_test = dr.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/a').text
        # dr.quit()
        if(index_test == "扫码登录"):
            pass
        else:
            raise EnvironmentError("登出当前账号失败")
