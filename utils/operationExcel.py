import xlrd
#注意xlrd2.0 版本以上不支持.xlsx格式
from common.public import filePath
#读取excel表数据
class OperationExcel:
    #获取sheet表
    def getSheet(self):
        book = xlrd.open_workbook(filePath())#common.public中已经将文件参数传入，所以不用传参
        # book =xlrd.open_workbook(str("E:\HUI\APITest\data\data.xls")) 上句代码相当于这句
        print(filePath())
        return book.sheet_by_index(0)#根据索引获取到sheet表

    #以列表形式读取出所有数据
    def getExceldatas(self):
        data = []
        title = self.getSheet().row_values(0)#获取表格第一行数据
        for row in range(1,self.getSheet().nrows):#从第二行开始获取数据
            row_value = self.getSheet().row_values(row)
            data.append(dict(zip(title,row_value)))#将读取出每一条用例数据组成字典，并添加到列表中
        return data

class ExcelVarles:
    case_Id="用例ID"
    case_module="用例模块"
    case_name = "用例名称"
    case_url = "用例地址"
    case_method = "请求方式"
    case_type="请求类型"
    case_data = "请求参数"
    case_headers = "请求头"
    case_preposition="前置条件"
    case_isRun = "是否执行"
    case_code = "状态码"
    case_result = "期望结果"
