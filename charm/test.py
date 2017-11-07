import requests,json,time,csv

url ='http://m.itslaw.com/mobile/judgements?conditions=searchWord%2B%E5%B9%BF%E5%91%8A%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7%2B1%2B%E5%B9%BF%E5%91%8A%E5%90%88%E5%90%8C%E7%BA%A0%E7%BA%B7&sortType=1&startIndex=20&countPerPage=20&_=1487513037808'
html=requests.get(url)
json_file = json.loads(html.text)
for i in json_file['data']['searchResult']['judgements']:
    # if i.has_key('keywords'):
    #     print(i['keywords'])
    # else:
    #     print('XXXXXXXXXXXX')
    print(i.setdefault('keywords'))
