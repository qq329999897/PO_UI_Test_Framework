#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2020/5/8 9:37 下午

import os
import unittest
from common import HTMLTestReportCN
from common.config_utils import local_config
from common import zip_utils
from common.email_utils import EmailUtils

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join( current_path , '..' , local_config.case_path )
report_path = os.path.join( current_path , '..' , local_config.report_path )

class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = '禅道自动化测试报告'
        self.description = 'newdream—test'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir = self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='liusir')
        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__ == '__main__':
    dir_path = RunAllCases().run()
    report_zip_path = dir_path+'/../禅道自动化测试报告.zip'
    zip_utils.zip_dir( dir_path , report_zip_path )
    EmailUtils('自动化测试报告（正式版）','python自动化测试报告',report_zip_path).send_mail()







