from pymongo import MongoClient



Client = MongoClient('localhost',27017)
test = Client['test']
icplist =test['icplist']


full_list = []
for i in icplist.find():
    full_list.append(i['证号'])
print(len(full_list))

n_list=list(set(full_list))
print(len(n_list))

for i in n_list:
    for y in icplist.find(i):
        print(y)