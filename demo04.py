#方法的封装   在demo05.py中调用
import re
import xlrd

def readexcle(exclename,sheetname):
    """
    这是一个用来读取excle表格的方法
    """
    excle = xlrd.open_workbook(exclename)#打开excle表，获取整个表的信息
    table = excle.sheet_by_name(sheetname)#选择对应的sheet表
    x = table.nrows #获取一共有多少行
    tablelist = []
    for i in range(x):
        rowlist = table.row_values(i)
        tablelist.append(rowlist)

    return tablelist

"""
datas = readexcle("testdata.xlsx","Sheet1")
print(datas[0][3])


xx = readexcle("yang.xlsx","yang1")
print(xx)

"""