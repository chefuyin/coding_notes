from django.shortcuts import render
from django.contrib.auth.models import User
# from django.http import HttpRequest,HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,RequestContext #csfr_token使用


# Create your views here.

def hello(request):
    # 标签使用
    user_list = User.objects.all()
    athlete = '0'
    athlete_list =[1,2,3,4,5,6]
    aaaaadfddddsdf=99
    # return render_to_response('table.html', locals(),context_instance=RequestContext(request))#context_instance好像有误
    return render(request,'table.html',locals())


    # print(isinstance(request,HttpRequest))#可以利用isinstance来判断request是否属于httprequest
    # print(request.path)#可以利用.path来查看path
    # print(request.method)#可以利用method来查看请求方式
    ##默认方法
    # user_list = User.objects.all()
    # return render(request,'table.html',{'user_list':user_list})

    ##自行构造response的方法一
    # from django.template import loader
    # from django.http import HttpResponse
    # user_list = User.objects.all()
    # t=loader.get_template('table.html')
    # c={'user_list':user_list}
    # return HttpResponse(t.render(c,request),content_type='text/html')

    #自行构造response的方法二，使用render_to_response
    # from django.shortcuts import render_to_response
    # user_list = User.objects.all()
    # return render_to_response('table.html',{'user_list':user_list})

    # #使用redirect跳转
    # from django.shortcuts import redirect
    # return redirect('/index')

    #使用locals传递函数
    # user_list = User.objects.all()
    # print(user_list.query)
    # print(locals())
    # return render(request, 'table.html', locals())






def index(request):
    return render(request,'index.html')