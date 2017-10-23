from aip import AipSpeech
import pyaudio
import wave
import requests as r
import pycurl,json

#官方文档的新方法，比老师的简单



# def get_file_content(filePath):
#     with open(filePath,'rb') as fp:
#         return fp.read()
#
# def use_cloud():
#     APP_ID = '10078949'
#     API_KEY = 'MrSZhgE9Biva1vWXQwgQsckZ'
#     SECRET_KEY = 'c3768c6ea1324ad4dc8279f1a80c0193'
#     aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#     result=aipSpeech.asr(get_file_content('2017-09-02_19_59_11.wav'),'wav',8000,{'lan':'zh',})
#     my_list = result['result']
#     print(my_list[0])
#
# use_cloud()

#老师的教程，出现参数错误
# def dump_res(buf):
#     print(buf)
#     my_temp=json.loads(buf)
#     print(my_temp)
#     # my_list=my_temp['result']
#     # print(type(my_list))
#     # print(my_list[0])
#
# def get_token():
#     apiKey ='MrSZhgE9Biva1vWXQwgQsckZ'
#     secretKey ='c3768c6ea1324ad4dc8279f1a80c0193'
#     auth_url ='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id='+apiKey+'&client_secret='+secretKey
#
#     res =r.get(auth_url).text
#     # print(json.loads(res)['access_token'])
#     return json.loads(res)['access_token']
#
#
# def use_cloud(token):
#     fp=wave.open('2017-09-02_19_59_11.wav','rb')
#     nf = fp.getnframes()
#     print('sampwidth:',fp.getsampwidth())
#     print('framerate:',fp.getframerate())
#     print('channels:',fp.getnchannels())
#
#     f_len=nf*2
#     audio_data = fp.readframes(nf)
#
#     cuid ='10078949'
#     srv_url='http://vop.baidu.com/server_api?cuid='+cuid+'&token='+token
#     http_header =[
#         'Content-Type:audio/pcm;rate=8000',
#         'Content-Length:{}'.format(f_len)
#     ]
#     c=pycurl.Curl()
#     c.setopt(pycurl.URL,str(srv_url))
#     c.setopt(c.POST,1)
#     c.setopt(c.TIMEOUT,80)
#     c.setopt(c.CONNECTTIMEOUT,80)
#     c.setopt(c.WRITEFUNCTION,dump_res)
#     c.setopt(c.POSTFIELDS,audio_data)
#     c.setopt(c.POSTFIELDSIZE,f_len)
#     c.perform()
#
# use_cloud(get_token())


#利用Python进行音频播放
# chunk =1024
# wf =wave.open('2017-09-02_19_59_11.wav','rb')
# p = pyaudio.PyAudio()
#
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),rate =wf.getframerate(),
#                 output=True)
# while True:
#     data = wf.readframes(chunk)
#     if data =="":break
#     stream.write(data)
# stream.close()
# p.terminate()



# 利用Python进行录音
# import wave
# from pyaudio import PyAudio,paInt16
# import datetime
#
# framerate =8000
# NUM_SAMPLES =2000
# channels =1
# sampwidth=2
# TIME=1
#
# def save_wave_file(filename,data):
#     with wave.open(filename,'wb')as wf:
#         wf.setnchannels(channels)
#         wf.setsampwidth(sampwidth)
#         wf.setframerate(framerate)
#         wf.writeframes(b''.join(data))#data里的都是byte，所以join时候要加上b在前面
#
# def my_record():
#     pa =PyAudio()
#     my_buf=[]
#     stream= pa.open(format=paInt16,channels =1,
#                     rate = framerate,input=True,
#                     frames_per_buffer = NUM_SAMPLES,)
#     count =0
#     while count < TIME*20:
#         stream_audio_data =stream.read(NUM_SAMPLES)
#         # print(stream_audio_data)
#         my_buf.append(stream_audio_data)
#         count+=1
#         print('.')
#     time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace("-","_").replace(" ","_").replace(":","_")
#     # print(time_tag+'.wav')
#     #以时间戳命名，省却命名烦恼
#     save_wave_file(time_tag+'.wav',my_buf)
#     stream.close()
#
# my_record()
#
# print('over!')





