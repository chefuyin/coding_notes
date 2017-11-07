import requests,json
class ILawContent():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
            'Cookie': 'JSESSIONID=C54EB1AC642C766922D54AAC66ACF5F9; gr_user_id=349f6505-3cf1-4b24-9777-b3321e1b470f; sessionId=36250226-033c-478e-b3a1-2f3e8e1e87f5; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1490585952,1490587037,1490600642,1490600946; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1490600946; persistenceId=""; Hm_lvt_7d9886d06cb8d83a4bbe76d3b68790bf=1490600779; Hm_lpvt_7d9886d06cb8d83a4bbe76d3b68790bf=1490603329',
        }
    def main(self):
        html_text = self.get_content()
        json_dict = self.html2json(html_text)
        data = self.get_case_content(json_dict)
        # print(json_dict)
        # print(type(json_dict))


    def get_content(self):
        self.case_url ='http://m.itslaw.com/mobile/judgements/judgement/76c3fc8a-870a-4c60-a158-6c86f1567df4?'
        html_json = requests.get(self.case_url,headers = self.headers)
        return html_json.text

    def html2json(self,html_text):
        json_dict = json.loads(html_text)#json格式转换为dict
        return json_dict

    def get_case_content(self,json_dict):
        case_content_data_list=[]
        for k in json_dict['data']['fullJudgement']:#从dict中提取有用信息
            for v in k:
                i=v['id']
                print(i)




a = ILawContent()
# print(a.get_content())
a.main()