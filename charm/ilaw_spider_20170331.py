#coding:utf-8
from bs4 import BeautifulSoup
import requests,json,time,csv,random
class ILawContent():
    def __init__(self):
        self.headers = {
            # 'User-Agent': random.choice(self.user_agent()),
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Cookie': 'gr_user_id=ea85e69b-7976-42ad-87a6-36727e5477b2; sessionId=d23e56cf-30f9-4875-802b-dad7d817f3ca; showSubSiteTip=false; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1487512023,1487512057; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1487512057; gr_session_id_8d9004219d790ea8=ef8e5a7c-8e92-4c7c-a86e-2f319399cbc5; subSiteCode=bj; collapsible=%2CsearchWord%2Ccase-reason%2Ccase-class%2Clocation%2Creferee-date%2Ctrial-procedure%2Cdoc-type',
        }
        self.site = 'http://m.itslaw.com/mobile/judgements/judgement/'
        # self.url = 'http://m.itslaw.com/mobile/judgements/judgement/76c3fc8a-870a-4c60-a158-6c86f1567df4'
        self.write_csv_file_header()
        self.start_page = int(input('Start page is(≥1):'))-1
        self.end_page = int(input('End page is((≥1)):'))


    def main(self):
        time1 = time.clock()
        try:
            # print(self.generate_url())
            url_list =[]
            # print(len(self.generate_page_url()))
            for url in self.generate_page_url():
                json_dict = self.html2json(self.get_html(url))
                # print(self.get_case_info(json_dict))
                case_url = self.get_case_list(json_dict)
                print(case_url)
                if case_url != None:#判断是否已经到最后一页
                    url_list=url_list+case_url
                    time.sleep(4)
            # print(len(url_list))
            for i in url_list:
                with open('url.txt','a+',encoding='utf-8') as file:
                    file.write(i+'\n')
            # print(url_list)
            # print(len(url_list))
            for case in url_list:
                html = self.get_html(case)
                json_dict1=self.html2json(html)
                case_data = self.get_full_judgement(json_dict1)
                # print(case_data)
                self.write_csv_file_content(case_data)
                print('you have got {} cases'.format(str(self.counter())))
                time.sleep(4)
        except Exception as e:
            print(e)
            pass
        time2 =time.clock()
        print('Mission accomplished!Cost {} seconds. '.format(str(time2-time1)))

    # def user_agent(self):
    #     user_agent =[
    #         'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1',
    #         'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    #         'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.31',
    #         'Opera/9.80 (Android 4.0.3; Linux; Opera Mobi/ADR-1210241554) Presto/2.11.355 Version/12.10',
    #         'SAMSUNG-SGH-G508E/G508EZCIG2 SHP/VPP/R5 NetFront/3.4 Qtv5.3 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1',
    #         'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3',
    #         'IUC(U;iOS 5.1.1;Zh-cn;320*480;)/UCWEB8.9.1.271/42/800',
    #     ]
    #     return user_agent

    def counter(self):
        count = [0]
        next = count[-1] + 1
        count.append(next)
        return count[-1]

    def generate_page_url(self):
        page_url_list =[]
        for i in range(self.start_page,self.end_page):
            base_url ='http://m.itslaw.com/mobile/judgements?conditions=searchWord%2B%E5%8C%97%E4%BA%AC%E5%B8%82%E9%93%B8%E6%88%90%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80%2B1%2B%E5%8C%97%E4%BA%AC%E5%B8%82%E9%93%B8%E6%88%90%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80&sortType=1&startIndex={}&countPerPage=20'.format(str(i*20))#无讼数据接口，返回的是json数据
            page_url_list.append(base_url)
        # print(page_url_list)
        return page_url_list

    def get_html(self,url):
        html =requests.get(url,headers=self.headers)#获取json信息
        # print(html.text)
        # soup =BeautifulSoup
        return html.text

    def html2json(self,html_text):
        json_dict = json.loads(html_text)#json格式转换为dict
        # print(json_dict)
        return json_dict

    def get_case_list(self, json_dict):
        case_url_list=[]
        if json_dict['data']['searchResult'].get('judgements','null')=='null':
            pass
        else:
            for i in json_dict['data']['searchResult']['judgements']:#从dict中提取有用信息
                case_url=self.site + i['id']
                case_url_list.append(case_url)
            return case_url_list

    def get_full_judgement(self,json_dict):
        # list =[]
        # l=[]
        # print(json_dict)
        i =json_dict['data']['fullJudgement']
        if i.get('court','null')=='null':
            court_name = 'null'
        elif i['court'].get('name','null')=='null':
            court_name= 'null'
        else:
            court_name=i['court']['name']

        if i.get('reason','null')=='null':
            reason = 'null'
        elif i['reason'].get('name','null')=='null':
            reason= 'null'
        else:
            reason=i['reason']['name']

        if i.get('judges','null')=='null':
            judges ='null'
        else:
            judges=[k['name'] for k in i['judges']]

        if i.get('proponents','null')=='null':
            proponents ='null'
        else:
            proponents=[k['name'] for k in i['proponents']]

        if i.get('opponents','null') =='null':
            opponents = 'null'
        else:
            opponents=[k['name'] for k in i['opponents']]

        if i.get('opponentLawyers','null') =='null':
            opponentLawyers = 'null'
        else:
            opponentLawyers = []
            for k in i['opponentLawyers']:
                if k.get('name', 'null') == 'null':
                    lawyer_name = 'null'
                else:
                    lawyer_name = k['name']
                if k.get('lawFirm', 'null') == 'null':
                    lawfirm = 'null'
                else:
                    lawfirm = k['lawFirm']
                lawyer = lawyer_name + ',' + lawfirm
                opponentLawyers.append(lawyer)
            # opponentLawyers=[k['name'] for k in i['opponentLawyers']]

        if i.get('proponentLawyers','null') =='null':
            proponentLawyers = 'null'
        else:
            proponentLawyers=[]
            for k in i['proponentLawyers']:
                if k.get('name', 'null') == 'null':
                    lawyer_name = 'null'
                else:
                    lawyer_name = k['name']
                if k.get('lawFirm', 'null') == 'null':
                    lawfirm = 'null'
                else:
                    lawfirm = k['lawFirm']
                lawyer = lawyer_name + ',' + lawfirm
                proponentLawyers.append(lawyer)
            # proponentLawyers = [k['name'] + ',' + k['lawFirm'] for k in i['proponentLawyers']]有报错，不得已拆分

        if i.get('otherLawyers','null') =='null':
            otherLawyers = 'null'
        else:
            otherLawyers = []
            for k in i['otherLawyers']:
                if k.get('name', 'null') == 'null':
                    lawyer_name = 'null'
                else:
                    lawyer_name = k['name']
                if k.get('lawFirm', 'null') == 'null':
                    lawfirm = 'null'
                else:
                    lawfirm = k['lawFirm']
                lawyer = lawyer_name + ',' + lawfirm
                otherLawyers.append(lawyer)
            # otherLawyers=[k['name']+','+k['lawFirm'] for k in i['otherLawyers']]

        data ={
        'id':i['id'],
        'case_url':self.site+i['id'],
        'title':i.setdefault('title'),
        'judgementType':i.setdefault('judgementType'),
        'caseType':i.setdefault('caseType'),
        'trialRound':i.setdefault('trialRound'),
        # 'publishBatch':i.setdefault('publishBatch'),
        'judgementAbstract':i.setdefault('judgementAbstract'),
        'caseNumber':i.setdefault('caseNumber'),
        'judgementDate':i.setdefault('judgementDate'),
        'publishDate':i.setdefault('publishDate'),
        'publishTypeText':i.setdefault('publishTypeText'),
        'historicalJudgement':i.setdefault('historicalJudgement'),
        'court':court_name,
        'reason':reason,
        'judges':judges,
        'proponents':proponents,
        'opponents':opponents,
        'opponentLawyers':opponentLawyers,
        'proponentLawyers':proponentLawyers,
        'otherLawyers':otherLawyers,
        }
        return data

    def write_csv_file_header(self):
        with open('file.csv','a+',newline='',encoding='GB18030')as file:
            fieldnames = ['id','case_url','title','judgementType','caseType','trialRound' ,'judgementAbstract',
                          'caseNumber','judgementDate','publishDate','publishType','publishTypeText','court','reason',
                          'historicalJudgement','judges','proponents','opponents','opponentLawyers','proponentLawyers','otherLawyers']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    def write_csv_file_content(self, data):
        with open('file.csv','a+',newline='',encoding='GB18030')as file:#'gb2312' codec can't encode character '\u5586' in position 246,GB2312，GBK，GB18030，是兼容的，包含的字符个数：GB2312 < GBK < GB18030
            fieldnames = ['id','case_url','title','judgementType','caseType','trialRound' ,'judgementAbstract',
                          'caseNumber','judgementDate','publishDate','publishType','publishTypeText','court','reason',
                          'historicalJudgement','judges','proponents','opponents','opponentLawyers','proponentLawyers','otherLawyers']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # writer.writerows(data)
            writer.writerow(data)

a = ILawContent()
a.main()

