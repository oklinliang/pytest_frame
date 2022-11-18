from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#设置单位时间
def short_time():
    time.sleep(5)

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options = Options()
    chrome_options.add_argument("--kiosk")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    dr = webdriver.Chrome(options=chrome_options)
    dr.maximize_window()
    base_url = "https://dev.tihal.cn:6200/fe/login"
    dr.get(base_url)
    short_time()
    # 登录信息
    dr.find_element(By.ID,"account_no").send_keys("luojunfeng")
    dr.find_element(By.ID,"account_pwd").send_keys("ABCdef123")
    captcha = input("验证码:")
    dr.find_element(By.ID,"captcha").send_keys(captcha)
    dr.find_element(By.XPATH,'//*[@id="App"]/div/div/div/form/div[4]/div/div/div/button').click()
    # a = time.localtime(time.time())
    # if a.tm_hour >= 16 and a.tm_hour <= 18:
    #     time.sleep(60)
    #     dr.find_element(By.XPATH,'').click()
    short_time()

    while True:
        # start = time.time()
        # print(start)
        #每次循环均刷新一次页面
        dr.refresh()
        short_time()
        short_time()
        # 项目信息-电建国际
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        # 项目信息-东南非区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[2]/span[3]').click()
        short_time()
        # 项目信息 - 中东北非区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[4]/span[3]').click()
        short_time()
        # 项目信息 - 欧亚区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[5]/span[3]').click()
        short_time()
        # 项目信息 - 欧亚区域总部 - 巴基斯坦
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[5]/span[2]/span').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[8]/span[3]').click()
        short_time()
        # 项目信息 - 欧亚区域总部 - 巴基斯坦 - 巴基斯坦巴沙大坝标项目
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[8]/span[2]/span').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[14]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[5]/span[2]/span').click()
        short_time()
        # 项目信息 - 电建国际 - 法律法规
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/ul/li[2]/span').click()
        short_time()
        # 项目信息 - 电建国际 - 法律法规 - 规章
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[3]/span[2]/span').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[3]/span[2]/span').click()
        short_time()
        # 项目信息 - 电建国际 - 法律法规 - 集团制度
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[4]/span[2]/span').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[4]/span[2]/span').click()
        short_time()
        # 项目信息 - 电建国际 - 法律法规 - 国际公司
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[5]/span[2]/span').click()
        short_time()
        # 项目信息 - 电建国际 - 法律法规 - 国际公司 - 关于印发《中国电力建设股份有限公司安全生产标准化自评管理办法》的通知
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[6]/span[3]/span').click()
        short_time()

        # 项目信息 - 国际公司 - 预案管理 - 集团
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/ul/li[3]/span').click()
        short_time()
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[1]/span[2]/span').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[1]/span[2]/span').click()
        short_time()
        # 项目信息 - 国际公司 - 预案管理 - 电建国际公司
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[2]/span[2]/span').click()
        short_time()
        # 项目信息 - 国际公司 - 预案管理 - 电建国际公司 - 国际工程项目HSE组织机构和职责标准
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div/div[3]/span[3]/span').click()
        short_time()

        # 项目信息 - 电建国际 - 国别风险
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/ul/li[4]/span').click()
        short_time()
        # 项目信息 - 电建国际 - 国别风险 - 风险可视化
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[2]/button').click()
        short_time()
        # 项目信息 - 电建国际 - 国别风险 - 尼日利亚（国别信息）
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[52]/div[1]/a').click()
        short_time()
        short_time()
        dr.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/button/span').click()
        short_time()

        # 项目信息 - 电建国际 - 安保信息
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/ul/li[8]/span').click()
        short_time()
        dr.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/button/span').click()
        short_time()

        # 舆情预警 - 安全周报
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[1]/ul/li[3]/span').click()
        short_time()
        # 舆情预警 - 安全周报 - 预警信息第一条
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/li[1]').click()
        short_time()
        dr.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/button/span').click()
        short_time()
        # 舆情预警 - 预警等级
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[2]').click()
        short_time()
        # 舆情预警 - 东南非区域总部 - 风险可视化
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[2]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[5]/div/button').click()
        short_time()
        # 舆情预警 - 中东北非区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[4]/span[3]').click()
        short_time()
        # 舆情预警 - 欧亚区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[5]/span[3]').click()
        short_time()
        # 舆情预警 - 亚太区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[6]/span[3]').click()
        short_time()
        # 舆情预警 - 美洲区域总部
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[7]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[5]/div/button').click()

        # 电建国际 - 应急指挥 - 周边资源
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[1]/ul/li[1]/span').click()
        short_time()
        # 电建国际 - 应急指挥 - 应急组织 - 滚动
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/a[2]').click()
        short_time()
        # 电建国际 - 应急指挥 - 应急物资 - 滚动
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/a[3]').click()
        short_time()
        # 电建国际 - 应急指挥 - 应急装备 - 滚动
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/a[4]').click()
        short_time()

        # 中西非区域总部 - 应急资源
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[3]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/ul/li[5]/span').click()
        short_time()
        # 美洲区域总部 - 应急资源
        dr.find_element(By.XPATH, '//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[3]/div/div/div/div[7]/span[3]').click()
        short_time()
        dr.find_element(By.XPATH,'//*[@id="authViewer"]/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/ul/li[5]/span').click()
        short_time()
        # end = time.time()
        # print(end)
        # print(end-start)





    short_time()
    dr.quit()