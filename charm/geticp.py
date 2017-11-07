import requests
from bs4 import BeautifulSoup
import lxml.html


class IcpSpider():
    def __init__(self):
        self.url = 'https://tsm.miit.gov.cn/pages/EnterpriseSearchList_Portal.aspx?PageNo=6'

    def get_info(self):
        url = self.url
        wb_data = requests.get(url,verify =False)#HTTPS链接，证书失效，只能跳过验证
        print(wb_data.text)
        # soup = BeautifulSoup(wb_data.text,'lxml')
        # print(soup)
        # company_name = soup.select('tbody > tr > td')
        selector = lxml.html.fromstring(wb_data.text)
        company_name = selector.xpath('//tr[class="tableList_Alter"]/tr')
        print(company_name)

a= IcpSpider()
a.get_info()