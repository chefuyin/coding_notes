import lxml.html
import requests,time,csv
from bs4 import BeautifulSoup
# from pymongo import MongoClient
# client = MongoClient('localhost',27017)
# icp = client['icp']
# icp_list = icp['icp_list20170123']


class GetIcpSpider() :

     def __init__(self):
        self.headers ={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Cookie':'pgv_pvi=80745472; _gscu_1912953156=83605315nsjoz783'
        }

     def get_page(self):
        url_list =[]
        for page in range(4057,5280):
            url = 'https://tsm.miit.gov.cn/pages/EnterpriseSearchList_Portal.aspx?&pageNo='+str(page)
            url_list.append(url)
        return url_list


     def check_flag(self,url):
         wb_data = requests.get(url, verify=False)  # https证书过期，修改verify为False
         print(url.split('=')[1])
         # selector = BeautifulSoup(wb_data.text, 'lxml')
         selector = lxml.html.fromstring(wb_data.text)
         busy_span = selector.xpath('//span[@class="urlpath"]/text()')
         for i in busy_span:
             if i=='系统提示 >>':
                 return False
         # for span in busy_span:
         #     print(span.get_text().strip())

     def write_file_head(self):
         with open('icp_list.csv', 'a+', newline='') as file:
             fieldnames = ['company_name', 'icp_num', 'area', 'available']
             writer = csv.DictWriter(file, fieldnames=fieldnames)
             writer.writeheader()  # 因为涉及多页时重复写入头信息会浪费，故一次写入，后续只写入信息

     def write_file(self, data):
         with open('icp_list.csv', 'a+', newline='') as file:
             fieldnames = ['company_name', 'icp_num', 'area', 'available']
             writer = csv.DictWriter(file, fieldnames=fieldnames)
             # writer.writeheader()
             writer.writerows(data)  # writerows与writerow不同，writerows可以写入字典，相对高效

     def get_icp(self):
         for url in self .get_page() :
            print(url.split('=')[1])
            # if self.get_flag(url):
            wb_data = requests.get(url, verify = False,headers = self.headers)   # https证书失效，验证需要修改为False
            selector = BeautifulSoup(wb_data.text,'lxml')
            infos = selector.find_all( 'td' )
            # info_list=[]
            num = 1
            for i in infos[:-2]:
                # print(i.get_text().strip())
                with open('icp_list.txt','a+') as file:
                    if num%5 ==0:
                        file.write(i.get_text().strip()+'&')
                        file.write('\n')

                    else:
                        file.write(i.get_text().strip() + '&')
                num+=1


            # info_list = []
            # for i in infos[:-2] :
            #     info = i.get_text().strip()
            #     # if info == '':
            #     #    pass
            #     # elif info == '查看' :
            #     if info=='查看':
            #        pass
            #     else :
            #        info_list.append(info)
            # print(info_list)
            # for x in range (0,10) :
            #     data = {
            #      'company_name' : info_list[x * 4 ],
            #      'icp_num' : info_list[(x * 4 ) + 1 ],
            #      'area' : info_list[(x * 4 ) + 2 ],
            #      'available' : info_list[(x * 4 ) + 3 ],
            #     }
            #     print(data)
                # self.write_file_head()
                # self.write_file(data)
            # info_list.clear()
     # else:
     #     pass
            time.sleep(3)
a = GetIcpSpider()
a.get_icp()
