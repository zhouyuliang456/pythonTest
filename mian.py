import urllib
import json
import xlrd

def http_post(contractIDs ):
    url = "http://"  #此处是要访问的url地址

    for i in range (0,len(contractIDs)):
     values = {"contractId": contractIDs[i]}
     jdata = json.dumps(values)  # 对数据进行JSON格式化编码
     req = urllib.Request(url, jdata)  # 生成页面请求的完整数据
     response = urllib.urlopen(req)
     print(response)

def read_excel():
   xls = xlrd.open_workbook('/Users/zhouyuliang/Downloads/zyl.xlsx')
   sheet = xls.sheet_by_name('Sheet1')
   cols = sheet.col_values(0)
   return cols

contractIds = read_excel()
http_post(contractIds)

