import requests
# from bs4 import BeautifulSoup
from lxml import html
class GdLawyer():

    def __init__(self):
        self.requests_url ='http://www.gdlawyer.gov.cn:91/websuite/query/queryLawyerList.jsp'
        self.headers ={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Cookie':'JSESSIONID=D5pqYl2QF2r5nDP59NZ3xGjqyS62Tc0BG8MczQX7NkVGvknKjCDR!261601972',
        }

    def generate_requests_data(self,pagenum):
        requests_data ={
            'currPageNo':'',
            'pageNo':str(pagenum),
            'queryType':'',
            'personChineseName':'',
            'qualificationNo':'',
            'certificateNo':'',
            'officeName':'',
            }
        return requests_data

    def get_content(self):
        content =requests.post(self.requests_url,headers=self.headers,data=self.generate_requests_data(2))
        selector = html.fromstring(content.text)
        ids = selector.xpath('//tr[@align="center"]/td[@height="25"]/a/@onclick')
        names =selector.xpath('//tr[@align="center"]/td[@height="25"]/a/text()')

        # for id in ids:
        #     print(id.replace('openWindow(','').replace(')',''))
        texts = selector.xpath('//tr[@align="center"]/td/text()')
        print(len(ids),len(names),len(texts),)
        for text in texts:
            if text !=' ':
                print(text)



# for i in range(1, 2239):
a=GdLawyer()
a.get_content()