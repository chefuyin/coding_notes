import os,re
from pymongo import MongoClient
client = MongoClient('localhost',27017)
charm = client['charm']
law_num2con_num =charm['law_num2con_num20170227']
def extra_law_num(filename):
    a= re.findall(r'(\W*[0-9]+)\w*', filename)#匹配法务合同号
    for b in a:
        if len(b)==10:#法务合同号为十位数
           return b#匹配成功就返回该值
def rename(doc_path):
    filelist=os.listdir(doc_path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(doc_path,files)#原来的文件路径
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue
        law_num_name=os.path.splitext(files)[0]#文件名
        law_num = extra_law_num(law_num_name)#提取法务合同号
        filetype=os.path.splitext(files)[1]#文件扩展名
        # # print(law_num)
        # if law_num != None :# print(law_num)
        for item in law_num2con_num.find({'law_num':law_num}):#匹配MONGO数据库里的合同号
            con_num = item['con_num']#通过查找法务合同号，匹配系统号
            Newdir=os.path.join(doc_path,con_num+filetype)#新的文件路径
            os.rename(Olddir,Newdir)#重命名

path =input('input doc path:')
rename(path)