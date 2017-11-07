import xlrd
from pymongo import MongoClient
client = MongoClient('localhost',27017)
charm = client['charm']
law_num2con_num =charm['law_num2con_num20170227']

data = xlrd.open_workbook('C://Users/chefy/Desktop/lawnum.xlsx')
table =data.sheets()[0]#通过index查找表
nrows = table.nrows#获取行数
for i in range(1,nrows):#遍历所有行
    rows = table.row_values(i)#每行以list存储
    data = {
        'con_num':rows[0],
        'law_num':rows[1],
    }
    law_num2con_num.insert_one(data)#以键值对写入数据库
print('Done!')
# print(table.row_values(1),nrows)