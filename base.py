# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 0.5


    def findElement(self, loctor):
            # '''
            # :param self:
            # :param loctor:
            # :return:
            # args:
            # loctor 传元祖，如（"id","xx")
            #查找元素
            # '''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x:
    x.find_element(*loctor))
        # print("正在定位元素:方法是-->%s,   value值是-->%s"%(loctor[0]  ,loctor[1]))
        return element

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()

    def sendKeys(self, loctor, text, is_clear_first=False):
        '''
        is_clear_first默认为False，不清空输入框
        '''
        ele = self.findElement(loctor)
        if is_clear_first:
                ele.clear() # is_clear_first 为True的时候执行
        ele.send_keys(text)
        print("正在定位元素:方法是-->%s,   value值是-->%s，  传的值是-->%s"%  (loctor[0],loctor[1],text))


    def isSelected(self,locator):
        '''
        判断元素是否被选中，返回bool值
        '''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return  r

    def isElementExist(self,locator):
        '''单个元素判断是否存在'''
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExits(self,locator):
        '''多个元素判定存在'''
        eles = self.findElement(locator)
        n =len(eles)
        if n == 0:
            return False
        elif n == 1 :
            return True
        else:
            print("定位到多个元素%s"%n)
        return True



