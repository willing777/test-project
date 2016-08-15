#coding=utf-8
'''
Created on 2016年8月10日

@author: dmrj
'''
import unittest
import HTMLTestRunner
import time

def creatsuite():
    testunit=unittest.TestSuite()
#定义测试文件查找的目录
    test_dir='D:\\workspace\\test_project\\test_case'
#定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,pattern ='test_*.py',top_level_dir=None)
#discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit
alltestnames = creatsuite()
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = 'D:\\workspace\\test_project\\report' + now + 'result.html'
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'测试报告',
        description = u'用例的执行情况')
    
    runner.run(alltestnames)
    fp.close()