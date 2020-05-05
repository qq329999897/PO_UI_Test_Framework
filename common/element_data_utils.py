import os
import xlrd
from common.config_utils import local_config
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
excel_path = os.path.join( current_path,'../element_info_datas/element_infos.xlsx' )

class ElementdataUtils:
    def __init__(self,module_name,element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(element_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.row_count = self.sheet.nrows

    def get_element_info(self,page_name):
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 2) == page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                timeout_value = self.sheet.cell_value(i, 5)
                element_info['timeout'] = timeout_value if isinstance(timeout_value,float) else local_config.time_out
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__=="__main__":
    # s = ElementdataUtils('login_page')
    elements = ElementdataUtils('login').get_element_info('login_page')
    # print(elements)
    for e in elements.values():
        print( e )


