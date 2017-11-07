from bs4 import BeautifulSoup
import requests,json,time,csv
class IlawSpider():
    def __init__(self):
        self.headers ={
        'User-Agent':'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        'Cookie':'gr_user_id=ea85e69b-7976-42ad-87a6-36727e5477b2; sessionId=d23e56cf-30f9-4875-802b-dad7d817f3ca; showSubSiteTip=false; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1487512023,1487512057; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1487512057; gr_session_id_8d9004219d790ea8=ef8e5a7c-8e92-4c7c-a86e-2f319399cbc5; subSiteCode=bj; collapsible=%2CsearchWord%2Ccase-reason%2Ccase-class%2Clocation%2Creferee-date%2Ctrial-procedure%2Cdoc-type',
    }
        self.site_url='http://m.itslaw.com/mobile/judgements/judgement?id='
        self.write_csv_file_header()
        self.start_page = int(input('Start page is(≥1):'))-1
        self.end_page= int(input('End page is((≥1)):'))

    def main(self):
        # self.write_csv_file_header()
        time1= time.clock()
        try:
            # print(self.generate_url())
            for url in self.generate_url():
                json_dict = self.html2json(self.get_html(url))
                # print(self.get_case_info(json_dict))
                self.write_csv_file_content(self.get_case_info(json_dict))
                print('you have got {} cases'.format(str(self.counter()*20)))
                time.sleep(3)
        except Exception as e:
            print(e)
        time2 =time.clock()
        print('Mission accomplished!Cost {} seconds. '.format(str(time2-time1)))


    def counter(self,count=[0]):
        # count = [0]
        next = count[-1] + 1
        count.append(next)
        return count[-1]

    def generate_url(self):
        url_list =[]
        for page in range(self.start_page,self.end_page):
            base_url ='http://m.itslaw.com/mobile/judgements?conditions=' \
                      'lawFirm%2B13982%2B1%2B%E5%8C%97%E4%BA%AC%E5%B8%82%E9%93%B8%E' \
                      '6%88%90%E5%BE%8B%E5%B8%88%E4%BA%8B%E5%8A%A1%E6%89%80&sortType=1' \
                      '&startIndex={}&countPerPage=20'.format(str(page*20))#无讼数据接口，返回的是json数据
            url_list.append(base_url)
        return url_list

    def get_html(self,url):
        html =requests.get(url,headers=self.headers)#获取json信息
        # soup =BeautifulSoup
        return html.text

    def html2json(self,html_text):
        json_dict = json.loads(html_text)#json格式转换为dict
        return json_dict

    def get_case_info(self,json_dict):
        case_info_data_list=[]
        for  i  in json_dict['data']['searchResult']['judgements']:#从dict中提取有用信息
            # 使用dict.setdefault(key),如果key存在，则返回其value;否则插入此key，
            # 其value为default，并返回default;使用这个方法也永远不会触发KeyError
            case_info_data ={
            'ilaw_id': i.setdefault('id'),
            'ilaw_url':self.site_url+i.setdefault('id'),
            'title' :i.setdefault('title'),
            'casetype':i.setdefault('caseType'),
            'trialround' : i.setdefault('trialRound'),
            'judgementtype' :i.setdefault('judgementType'),
            'courtname':i.setdefault('courtName'),
            'casenum':i.setdefault('caseNumber'),
            'judgementdate' :i.setdefault('judgementDate'),
            'keywords' :i.setdefault('keywords'),
            'courtopinion':i.setdefault('courtOpinion'),#如果不确定是否有该key值，最好用dict.get['key']
            'publishdate' :i.setdefault('publishDate'),
            'publistype' :i.setdefault('publishType'),
            'history_judgement' :i.setdefault('hasHistoricalJudgment'),
            'similar_judgement' :i.setdefault('similarJudgement'),
            }
            case_info_data_list.append(case_info_data)#以列表存储方便后续多行写入
        return case_info_data_list

    def write_csv_file_header(self):
        with open('ilaw_file.csv','a+',newline='')as file:
            fieldnames = ['ilaw_id','ilaw_url','title','casetype','trialround' ,'judgementtype','courtname','casenum','judgementdate','keywords','courtopinion',
            'publishdate','publistype','history_judgement','similar_judgement',]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # 因为涉及多页时重复写入头信息会浪费，故一次写入，后续只写入具体信息

    def write_csv_file_content(self,data):
        with open('ilaw_file.csv','a+',newline='')as file:
            fieldnames = ['ilaw_id','ilaw_url','title','casetype','trialround' ,'judgementtype','courtname','casenum','judgementdate','keywords','courtopinion',
            'publishdate','publistype','history_judgement','similar_judgement',]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(data)


a= IlawSpider()
a.main()