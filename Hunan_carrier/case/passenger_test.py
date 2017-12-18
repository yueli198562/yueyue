#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select #引用Select 下拉框操作
from s.rexcel import *
import time,unittest


class Case(unittest.TestCase):  #测试用例类
    '''保费计算'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox() #启动火狐浏览器
        cls.driver.get(sheet1_B1)  #打开url
        driver=cls.driver
        driver.find_element_by_xpath(B1).send_keys(sheet1_B2)  #输入用户名
        driver.find_element_by_xpath(B2).send_keys(sheet1_B3)  #输入密码
        driver.find_element_by_xpath(B3).click()  #点击登录按钮
        #左侧菜单点击在线投保--在线投保
        driver.find_element_by_xpath(B4).click()
        driver.find_element_by_xpath(B5).click()
        #切换到ifame表单
        driver.switch_to_frame("iframe3")
        #点击立即投保
        driver.find_element_by_xpath(B6).click()
        time.sleep(2)
        #定位到checkbox标签，勾选所有checkbox复选框
        checkbox=driver.find_elements_by_xpath(B7)
        for i in checkbox:
            i.click()
        #点击同意并下一步
        driver.find_element_by_xpath(B8).click()
        time.sleep(2)
        #被保险人和投保人一致，选择单选框是
        driver.find_element_by_xpath(B9).click()
        #统一社会信用代码填写
        driver.find_element_by_xpath(B10).send_keys("aaaaaaa")
        #上传营业执照
        driver.find_element_by_xpath(B11).click()
        os.system(B12)
        #道路运输经营许可证输入框填写,和图片上传
        driver.find_element_by_xpath(B13).send_keys("aaaaaaa")
        driver.find_element_by_xpath(B14).click()
        os.system(B12)
        #运输地域范围下拉框选择
        s=driver.find_element_by_xpath(B15)
        Select(s).select_by_value(sheet1_B4)
        #客运经营范围选择
        a=driver.find_elements_by_xpath(B16)
        for i in a:
            if int(i.get_attribute("value"))==0==sheet1_B5:
                i.click()
                driver.find_element_by_xpath(B17).send_keys("aaaaaaaa")
            elif int(i.get_attribute("value")) == sheet1_B5:
                i.click()
        #点击【保存并添加车辆】按钮
        driver.find_element_by_xpath(B18).click()
        time.sleep(2)
        #点击填加车辆
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div/button").click()
        #点击新增                                                      
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='newAddbut']").click()
        #输入框添加车辆信息
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='carId']").send_keys(u"京j33345")
        driver.find_element_by_xpath("//*[@id='carType']").send_keys("ya")
        driver.find_element_by_xpath("//*[@id='engine']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='carNum']").send_keys("11123111")
        driver.find_element_by_xpath("//*[@id='seatNum']").send_keys("10")
        driver.find_element_by_xpath("//*[@id='myfilesF']").click()
        os.system(B12)
        time.sleep(2)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='formCar']/div/div/div[3]/button").click()
        #点击保存并下一步
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        #勾选车辆
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='tb']/tr/td[1]/input").click()
        #点击设定保期
        driver.find_element_by_xpath('//*[@data-target="#myModa1One"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@class="modal-footer"]/button').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test1(self):
        '''每人责任限额（40万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("40万")
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*112
        self.assertEqual(d, e)

    def test2(self):
        '''每人责任限额（50万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("50万")
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*125
        self.assertEqual(d, e)
        
    def test3(self):
        '''每人责任限额（60万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("60万")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*142
        self.assertEqual(d, e)
        
    def test4(self):
        '''每人责任限额（70万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("70万")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*162
        self.assertEqual(d, e)
        
    def test5(self):
        '''每人责任限额（80万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("80万")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*174
        self.assertEqual(d, e)
        
    def test6(self):
        '''每人责任限额（90万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("90万")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*184
        self.assertEqual(d, e)
        
    def test7(self):
        '''每人责任限额（100万元）'''
        driver=self.driver
        #选择方案
        driver.find_element_by_xpath('//*[@data-target="#myModa1Two"]').click()
        time.sleep(2)
        s1=driver.find_element_by_xpath("//select")
        Select(s1).select_by_visible_text("100万")
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='myModa1Two']/div/div/div[3]/button").click()
        time.sleep(2)
         
        a=int(driver.find_element_by_xpath("//*[@id='tb']/tr/td[4]").text) #载人人数
        c=int(driver.find_element_by_xpath("//*[@id='totalCarNum']").get_attribute("value")) #车辆合计
        d=int(driver.find_element_by_xpath("//*[@id='totalMoney']").get_attribute("value")) #保费合计
        e=a*c*202
        self.assertEqual(d, e)
    
if __name__=="__main__":
    unittest.main()  #运行所有测试用例




