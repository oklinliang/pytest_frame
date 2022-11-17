import lin_config
import re
import lin_chandao
from selenium.webdriver.common.keys import Keys
import json
import lin_random_module
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options
"""
    自动化程序
"""
class Test_xxx():
    def test_xx(self):
        a = ''.join(lin_random_module.hanzi(15))
        assert 1==2,lin_chandao.add_bug("title","steps")