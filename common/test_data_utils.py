#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_data_utils.py
# @time: 2020/5/8 8:29 下午

import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
test_data_path = os.path.join( current_path , '..' , local_config.testdata_path )

class TestDataUtils:

    def __init__(self,test_suite_name,test_file_name,test_class_name=None,test_data_path=test_data_path):
        test_data_path = os.path.join( test_data_path,test_suite_name,test_file_name+'.xlsx' )
        self.excel_data = ExcelUtils( test_data_path , test_class_name ).get_sheet_data_by_list()
        self.excel_rows = len(self.excel_data)

    def convert_exceldata_to_testdata(self):
        # {'test_login_success':
        #      {'test_name':'验证是否能成功进行登录','isnot':'是','excepted_result':'测试人员1','test_parameter':{'username':'test01','password':'newdream123'} }
        #  'test_login_fail':
        #      { }
        #  }
        test_data_infos = {}
        for i in range(1,self.excel_rows): # 1,2
            test_data_info = {}
            test_data_info[ 'test_name' ] = self.excel_data[i][1]
            test_data_info[ 'isnot' ] = False if self.excel_data[i][2].__eq__('是') else True
            test_data_info[ 'excepted_result' ] = self.excel_data[i][3]
            test_parameter = {}
            for j in range( 4, len(self.excel_data[i]) ):
                if self.excel_data[i][j].__contains__('=') and len( self.excel_data[i][j] ) > 2 :
                    parameter_info = self.excel_data[i][j].split('=')
                    test_parameter[ parameter_info[0] ] = parameter_info[1]
            test_data_info[ 'test_parameter' ] = test_parameter
            test_data_infos[ self.excel_data[i][0] ] = test_data_info
        return test_data_infos

if __name__ == '__main__':
    infos = TestDataUtils('login_suite','login_test').convert_exceldata_to_testdata()
    for i in infos.values():
        print( i )






