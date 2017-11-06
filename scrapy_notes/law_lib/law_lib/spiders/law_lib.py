import re
import scrapy
import requests
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import LawLibItem   #..为相对引用
import lxml.html
from urllib.parse import quote,unquote

class Myspider(scrapy.Spider):
    name='law_lib' #only one
    allowed_domains=['law-lib.com']
    base_url='http://law-lib.com/law/'
    department_index='bbdw-zy.htm'

    def start_requests(self):
        index_url=self.base_url+self.department_index
        req= requests.get(index_url)
        req.encoding='gb2312'
        selector=lxml.html.fromstring(req.text)
        urls=selector.xpath('//div[@class="law_df"]/p/a/@href')
        department_urls=[]
        for url in urls:
            if len(url.split('/'))==1:
                decode_url=url.split('=')[0]+'='+quote(url.split('=')[1],encoding='gb2312')
                url=self.base_url+decode_url
                department_urls.append(url)
            else:
                decode_url = url.split('=')[0] + '=' + quote(url.split('=')[1],encoding='gb2312')
                department_urls.append(decode_url)
        for url in department_urls:
            yield Request(url,self.parse)

    def parse(self, response):
        selector=lxml.html.fromstring(response.text)
        list_pages=selector.xpath('//p[@class="p_fenye"]/a/@href')
        list=[]
        for page in list_pages:
            if len(page.split('/'))==1:
                page=self.base_url+page
                list.append(page)
            else:
                list.append(page)
        list.append(response.url)
        print(list)
        # print(response.text)
