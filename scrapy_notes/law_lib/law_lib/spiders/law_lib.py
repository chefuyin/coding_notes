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
                page=self.base_url+page.replace('law_view.','law_view1.')
                list.append(page)
            else:
                list.append(page.replace('law_view.','law_view1.'))
        list.append(response.url)
        for url in list:
            yield Request(url,self.get_law_list)

    def get_law_list(self,response):
        selector=lxml.html.fromstring(response.text)
        law_list=selector.xpath('//ul[@class="law_list"]/li//span')
        for law in law_list:
            href=law[0].get('href')#law[0]==a标签
            if len(href.split('/'))==1:
                url=self.base_url+href
            else:
                url=href
            title=law[0].get('title')
            yield Request(url,self.get_law_page,meta={'title':title,'url':url})

    def get_law_page(self,response):
        selector = lxml.html.fromstring(response.text)
        db=selector.xpath('//div[@class="content_view"]/a/text()')
        if db=='':
            pass
        else:
            if db[-1]=='在线数据库':
                pass
            else:
                item=LawLibItem()
                item['law_lib_url']=response.meta['url']
                item['title']=response.meta['title']
                infos=selector.xpath('//ul[@class="left_conul"]/li/text()')
                item['department']=infos[1].split("】")[1]
                item['publish_number']=infos[2].split("】")[1]
                item['publish_date']=infos[3].split("】")[1]
                item['invalid_date']=infos[4].split("】")[1]
                item['source']=infos[5].split("】")[1]
                contents=selector.xpath('//div[@class="content_view"]/text()')
                content_list=[]
                for c in contents:
                    if c.strip()=='':
                        pass
                    else:
                        content_list.append(c.strip())
                content='\n'.join(content_list)
                item['content']=content
                return item





