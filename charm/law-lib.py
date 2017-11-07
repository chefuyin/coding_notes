import requests,lxml.html,random,time
from pymongo import MongoClient
from urllib import parse

class LawLibSpider():

    def __init__(self):
        self.dep_list =[
        '%C8%AB%B9%FA%C8%CB%C3%F1%B4%FA%B1%ED%B4%F3%BB%E1',
        '%C8%AB%B9%FA%C8%CB%C3%F1%B4%FA%B1%ED%B4%F3%BB%E1%B3%A3%CE%F1%CE%AF%D4%B1%BB%E1',
        '%D7%EE%B8%DF%C8%CB%C3%F1%B7%A8%D4%BA',
        '%D7%EE%B8%DF%C8%CB%C3%F1%BC%EC%B2%EC%D4%BA',
        '%B9%FA%CE%F1%D4%BA',
        '%B9%FA%CE%F1%D4%BA%B0%EC%B9%AB%CC%FC',]
        self.law_site ='http://law-lib.com/law/'
        self.header_list =[
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
        ]
        self.header = {'User-Agent': random.choice(self.header_list)}
        self.proxy_list = self.get_proxy_list()
        self.proxy = random.choice(self.proxy_list)
        self.client = MongoClient('loaclhost',27017)
        self.law_lib_db = self.client['law_lib_db']
        self.law_lib_ids = self.law_lib_db['law_lib_ids']

    def counter(self):
        i = [0]
        next = i[-1] + 1
        i.append(next)
        return i[-1]

    def get_proxy_list(self):
        kuaidaili='http://www.kuaidaili.com/free/'
        wb_data= requests.get(kuaidaili,headers=self.header)
        # print(wb_data.text)
        selector = lxml.html.fromstring(wb_data.text)
        # print(selector)
        ips = selector.xpath('//tr/td[@data-title="IP"]/text()')
        ports = selector.xpath('//tr/td[@data-title="PORT"]/text()')
        proxy_ips=[]
        for ip,port in zip(ips,ports):
            proxy_ip = ip+':'+port
            proxy_ips.append(proxy_ip)
        return proxy_ips

    def generate_law_page_url(self):
        law_page_urls =[]
        for dep_name in self.dep_list:
            law_page_url='http://www.law-lib.com/law/lawml.asp?bbdw={}'.format(dep_name)
            law_page_urls.append(law_page_url)
            # print(law_page_url)
        return law_page_urls

    def get_law_id(self):
        # proxy = '122.72.32.73:80'
        for law_url in self.generate_law_page_url():
            try:
                wb_data = requests.get(law_url,proxies=self.proxy,headers=self.header)
                selector =lxml.html.fromstring(wb_data.text)
                pages = selector.xpath('//p[@class="p_fenye"]/a')
                page_list =[law_url]
                for page in pages:
                    other_page=self.law_site+page.get('href')
                    page_list.append(other_page)
                for allpage in page_list:
                    page_data = requests.get(allpage, proxies=self.proxy, headers=self.header)
                    data =lxml.html.fromstring(page_data.text)
                    hrefs = data.xpath('//span[@class="spanleft"]/a')
                    for href in hrefs:
                        law_id =href.get('href')
                        data ={
                            'id':law_id.split('?')[1],
                            'url':self.law_site+law_id,
                        }
                        self.law_lib_ids.insert_one(data)
                        print('get{}ids:'.format(str(self.counter())))
                        time.sleep(2)
            except Exception as e:
                print(e)

# if __name__=='main':
a = LawLibSpider()
a.get_law_id()

