import json
import re
import pytest
from utils.operationExcel import OperationExcel
from utils.operationExcel import ExcelVarles
from base.method import ApiRequest
from utils.logger import Logger
import allure

log=Logger(__name__).get_log()

@allure.epic("xcf")
@pytest.mark.parametrize("data", OperationExcel().getExceldatas())
def test_api_all(data):
    #获取表格请求头数据 对请求头做为空处理并添加token
    headers = data[ExcelVarles.case_headers]
    if len(str(headers).split())== 0:
        pass
    elif len(str(headers).split())>= 0:
        headers = json.loads(headers)
        headers["Authorization"]="Bearer eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnQiOiJtYXN0ZXIiLCJsb2dpbl91c2VyX2tleSI6IjM4NDYxZTQ2LTkyODQtNDk2Ny1iYjdmLTllZDg4M2NjMTRhZSJ9.Oz8VrnOijzVUaZwIxfKR6ujbMCbdvMx2Gs9AOoMtD0wrdSFkclausubVQxHW0o39Q-SwaUTH5MVvdePamRnb1Q"
        headers["Cookie"]="Tenant-Key=master; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnQiOiJtYXN0ZXIiLCJsb2dpbl91c2VyX2tleSI6IjM4NDYxZTQ2LTkyODQtNDk2Ny1iYjdmLTllZDg4M2NjMTRhZSJ9.Oz8VrnOijzVUaZwIxfKR6ujbMCbdvMx2Gs9AOoMtD0wrdSFkclausubVQxHW0o39Q-SwaUTH5MVvdePamRnb1Q"
        headers=headers
        log.info(f"请求头为: {headers}")

    #获取请求参数并做为空处理
    params = data[ExcelVarles.case_data]

    if len(str(params).split())== 0:
        pass
    elif len(str(params).split())>= 0:
        params =params
        #把请求参数中的null替换为None 并去掉请求参数中的换行符
        #new_param=params.replace("null", "None") #注意字符串替换需要用新字符串替换旧字符串，不能直接用字符串替换
        #new_params=re.sub("\n","",new_param)
        #print(new_params)
        log.info(f"请求参数为: {params}")

    #断言封装
    case_code = int(data[ExcelVarles.case_code])
    def case_assert_result(response):
        assert response.json()["code"] == case_code# "状态码"
        assert data[ExcelVarles.case_result] in json.dumps(response.json(),ensure_ascii=False)#"响应数据" ensure_ascii=False便于打印或作为返回数据时正确显示中文
    #执行用例
    if data[ExcelVarles.case_method] == "get":
        response=ApiRequest().send_request(
            method=data[ExcelVarles.case_method],
            url=data[ExcelVarles.case_url],
            headers=headers,
            params=params)
        print(response.json())
        case_assert_result(response=response)
    elif data[ExcelVarles.case_method] == "post":
        response=ApiRequest().send_request(
            method=data[ExcelVarles.case_method],
            url=data[ExcelVarles.case_url],
            headers=headers,
            data=params)
        print(response.json())
        case_assert_result(response=response)

