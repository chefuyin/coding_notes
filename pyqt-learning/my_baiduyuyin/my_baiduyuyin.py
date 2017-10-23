# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog
from Ui_my_baiduyuyin import Ui_MainWindow
import sys,pyaudio,wave
from aip import AipSpeech
from pyaudio import PyAudio,paInt16
import datetime
# import threading
# from time import ctime
# from queue import Queue

#多线程测试，尚未成功
# class MyThread(threading.Thread):
#     def __init__(self,func,args,name=''):
#         threading.Thread.__init__(self)
#         self.name =name
#         self.func=func
#         self.args=args
#
#     def getResult(self):
#         return self.res
#
#     def run(self):
#         print('starting',self.name,'at:',ctime())
#         self.res=self.apply(self.func,self.args)#python3已经不支持apply了
#         print(self.name,'finished at:',ctime)
#
#     def apply(self,f,*args,**kw):#由于不再支持apply，所以重写了apply
#         return f(*args,**kw)



class MainWindow(QMainWindow, Ui_MainWindow):
# class MainWindow(QMainWindow, Ui_MainWindow,threading.Thread):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        # threading.Thread.__init__(self)
        self.setupUi(self)
        self.my_dir=''
        self.framerate =8000
        self.NUM_SAMPLES =2000
        self.channels =1
        self.sampwidth=2
        self.TIME=1

        # self.file_name_index =1
        # self.wave_queue =Queue(1024)

    # def run(self):
    #     print('starting',self.name,'at:',ctime())
    #     self.res=self.apply(self.my_record)#python3已经不支持apply了
    #     print(self.name,'finished at:',ctime)
    #
    # def apply(self,f,*args,**kw):#由于不再支持apply，所以重写了apply
    #     return f(*args,**kw)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.my_dir,my_file_ext = QFileDialog.getOpenFileName(self, '选择文件', '/')
        # print(self.my_dir)
        if self.my_dir =='':
            self.textBrowser.append('尚未选择文件！')
        else:
            self.textBrowser.append('已选择文件：{}'.format(self.my_dir))

    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            if self.my_dir =='':
                self.textBrowser.append('尚未选择文件，请先选择文件！')
            elif self.my_dir.split('.')[-1] == 'wav':
                chunk = 1024
                wf = wave.open(self.my_dir, 'rb')
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(), rate=wf.getframerate(),
                                output=True)
                # self.textBrowser.append('开始播放！')
                while True:
                    data = wf.readframes(chunk)
                    if data == "": break
                    stream.write(data)
                # self.textBrowser.append('播放完毕')
                stream.stop_stream()
                stream.close()
                p.terminate()


            else :
                self.textBrowser.append('不支持的文件格式，请重新选择.wav文件！')
        except Exception as e:
            self.textBrowser.append('出现错误：{}'.format(e))

    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        pass
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # pass
        self.textBrowser.append('开始录音：')
        self.my_record()



    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            if self.my_dir =='':
                self.textBrowser.append('尚未选择文件，请先选择文件！')
            elif self.my_dir.split('.')[-1] == 'wav':
                result= self.use_cloud(self.my_dir)
                self.textBrowser.append('语音识别完成，结果为：{}'.format(result))
            else :
                self.textBrowser.append('不支持的文件格式，请重新选择.wav文件！')
        except Exception as e:
            self.textBrowser.append('出现错误：{}'.format(e))

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def use_cloud(self,filePath):
        APP_ID = '10078949'
        API_KEY = 'MrSZhgE9Biva1vWXQwgQsckZ'
        SECRET_KEY = 'c3768c6ea1324ad4dc8279f1a80c0193'
        aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = aipSpeech.asr(self.get_file_content(filePath), 'wav', 8000, {'lan': 'zh', })
        my_list = result['result']
        return my_list[0]

    def save_wave_file(self,filename,data):
        with wave.open(filename,'wb')as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.sampwidth)
            wf.setframerate(self.framerate)
            wf.writeframes(b''.join(data))#data里的都是byte，所以join时候要加上b在前面

    def my_record(self):
        pa =PyAudio()
        my_buf=[]
        stream= pa.open(format=paInt16,channels =1,
                        rate = self.framerate,input=True,
                        frames_per_buffer = self.NUM_SAMPLES,)
        count =0
        while count < self.TIME*20:
            stream_audio_data =stream.read(self.NUM_SAMPLES)
            # print(stream_audio_data)
            my_buf.append(stream_audio_data)
            count+=1
            # print('.')
            self.textBrowser.append('.')

        #做多线程，暂时未测试成功
        # if my_buf:
        #     if self.file_name_index <11:
        #         pass
        #     else:
        #         self.file_name_index -=1
        #     filename = str(self.file_name_index)+'.wav'
        #     self.save_wave_file(filename=filename,data=my_buf)
        #     self.writeQ(queue=self.wave_queue,data = filename)
        #     self.file_name_index +=1
        #     print(filename,'saved!')
        # else:
        #     print('file not saved!')

        time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace("-","_").replace(" ","_").replace(":","_")
        print(time_tag+'.wav')
        #以时间戳命名，省却命名烦恼
        self.save_wave_file(time_tag+'.wav',my_buf)
        stream.close()
        # self.textBrowser.append('录音完毕，{}已存储！'.format(time_tag+'.wav'))
        
if __name__ == "__main__":    
    app = QApplication(sys.argv)   
    ui = MainWindow()
    # ui.setDaemon(True)#父线程结束至线程结束
    # ui.start()
    ui.show()
    sys.exit(app.exec_())
    
