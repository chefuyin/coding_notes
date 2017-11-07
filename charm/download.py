import requests,json,re,msvcrt,sys,datetime,xlrd
from bs4 import BeautifulSoup
class Downloader():
    def __init__(self):
        self.login_url ='http://192.168.0.37:8000/login.svc'
        self.role_select_url = 'http://192.168.0.37:8000/role_select.svc'
        self.contract_header_url = 'http://192.168.0.37:8000/autocrud/cont.CHARM_CON3060.charm_con_archiving/query?pagesize=10&pagenum=1&_fetchall=false&_autocount=true'
        self.attachment_url='http://192.168.0.37:8000/atm_download.svc?attachment_id='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Cookie': 'TARGETURL=modules/wfl/WFL1001/sys_favorite_function_view.screen; JSESSIONID=61668231E3A41251A72225507B7231B5.tomcat3; IS_NTLM=N; USERNAME=chefy; LANG=ZHS; ISTIMEOUT=false; vh=592; vw=1145'
        }
        self.s = requests.session()

    def main_control(self):
        self.login_sys()
        self.select_role()#浏览器中是自动跳转的，不选取会报错
        for contract_num in self.get_file_list():
            # contract_num =input('请输入系统合同号：\n')
            result=self.response_of_contract_info(contract_num)
            header_id = self.get_contract_header_id(result)
            upload_data = self.get_upload_page_info(header_id,contract_num)
            self.phase(upload_data,contract_num)

    def get_file_list(self):
        file_path =input('FILE PATH IS :').replace('\\','\/')
        file_info=xlrd.open_workbook(file_path)
        table = file_info.sheets()[0]  # 通过index查找表
        nrows = table.nrows  # 获取行数
        file_list=[]
        for i in range(1, nrows):  # 遍历所有行,含标题
            rows = table.row_values(i)  # 每行以list存储
            file_list.append(rows)
            # print(file_list)
        return file_list

        # print(len(file_list))
    # def password_input(self):
    ###密码隐藏只在cmd命令窗口可以用
    #     chars=[]
    #     while True:
    #         try:
    #             newchar=msvcrt.getch().decode(encoding="utf-8")
    #         except:
    #             return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
    #         if newchar in '\r\n':
    #             print('')
    #             break
    #         elif newchar =='\b':
    #             if chars:
    #                 del chars[-1]
    #                 msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格
    #                 msvcrt.putch(' '.encode(encoding='utf-8'))  # 输出一个空格覆盖原来的星号
    #                 msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格准备接受新的输入
    #
    #         else:
    #             chars.append(newchar)
    #             msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号
    #     print('')
    #     return ''.join(chars)

    def login_sys(self):
        # s= requests.session()
        print("username:")
        login_id = input()
        print("password:")
        password = input()
        # password = self.password_input()
        # print("\nyour password is:{0}".format(pwd))
        # input("按回车键退出")
        login_data = {
            '_request_data':'''{"parameter":{"user_name":'''+login_id+''',"user_password":'''+password+''',"user_language":"ZHS","language":"简体中文","is_ipad":"N"}}]'''
        }
        response = self.s.post(self.login_url,headers=self.headers,data=login_data)
        print('step1:系统已登录,系统状态为'+str(response.status_code))

    def select_role(self):
        role_data ={
            '_request_data':'{"parameter":{"role_id":65,"company_id":1,"role_company":"65_1","role_company_name":"法务人员-昌荣传播"}}'
        }
        role_response = self.s.post(self.role_select_url,data=role_data)
        print("step2:身份选取成功，系统状态为"+str(role_response.status_code))

    def response_of_contract_info(self,sys_con_num):
        date = datetime.datetime.now()
        today = date.strftime('%Y-%m-%d')
        # print(today)
        # print(type(today))
        sys_num=sys_con_num
        if sys_num is not str:
            sys_num_str =str(sys_num)
            requests_data = {
                '_request_data': '''{"parameter":{"creation_date_to":''' + today + ''',"sys_contract_number":''' + sys_num_str + '''}}'''
            }
        else:
            requests_data ={
                '_request_data':'''{"parameter":{"creation_date_to":'''+today+''',"sys_contract_number":'''+sys_num+'''}}'''
            }
        print(requests_data)
        result =self.s.post(self.contract_header_url,data=requests_data)
        print(result.content)
        # print(result.text)
        # return result.text

    def get_contract_header_id(self,result):
        j = json.loads(result)
        # contract_header_ids=j['result']['record']['contract_header_id']
        print(j)
        # for k in contract_header_ids:
        #     print(contract_header_ids)
        #     # print(type(j))
        #     return k

    def get_upload_page_info(self,contract_header_id,sys_num):
        upload_url ='http://192.168.0.37:8000/lawUploadFile.screen?table_name=CHARM_CONTRACT_HEADERS&header_id={}&sys_contract_number={}'.format(contract_header_id,sys_num)
        upload_html =self.s.get(upload_url)
        selector = BeautifulSoup(upload_html.text,'lxml')
        # print(selector)
        content = selector.select('body > script')
        data = content[0].text
        # print(data)
        return data

    def phase(self,data,sys_num):
        pattern = re.findall(r'"datas":(.*),"height"', data)
        for i in pattern:
            list = i.replace('[','').replace(']','').split(',')
            attachment_id =list[1]
            full_attachment_url =self.attachment_url+str(attachment_id)
            file_name =str(list[8]).replace('"','')
            upload_time =list[7]
            if file_name.split('.')[-1]=='pdf' or 'PDF':
                data_info={
                    'sys_con_num':sys_num,
                    'attachmen_url':full_attachment_url,
                    'upload_time':upload_time,
                    'file_name':sys_num+'_'+file_name
                }
                print(data_info)
            else:
                print("THERE IS 0 PDF FILE IN "+sys_num)
            # print(full_attachment_url,file_name,sep='\n')

        # print(pattern)
        # for i in content:
        #     data =i.text.replace('new Aurora.DataSet','').replace('(','').replace(')','')
        #     print(i.text)
        #     print(data)
        #     data_json = json.loads(data)
        #     print(data_json)
        # content = selector.xpath('//a[@target="_self"]')
        # print(content)
        # for file_name in content:
        #     print(file_name)

        # print(upload_html.text)

a= Downloader()
a.main_control()
# a.get_file_list()


# login_url ='http://192.168.0.37:8000/login.svc'
# request_url ='http://192.168.0.37:8000/autocrud/cont.CHARM_CON3060.charm_con_archiving/query?pagesize=10&pagenum=1&_fetchall=false&_autocount=true'
# # download_url =''
# request_data ={
#     '_request_data':'{"parameter":{"creation_date_to":"2017-02-27","sys_contract_number":"CON16110017"}}'
# }
#
#
# response =requests.post(request_url,data=request_data)
