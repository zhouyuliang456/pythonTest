import xlrd
def read_excel():
   print("ffds")
   xls = xlrd.open_workbook('/Users/zhouyuliang/Downloads/zyl.xlsx')
   sheet = xls.sheet_by_name('Sheet1')
   cols = sheet.col_values(0)
   print(cols)

read_excel()