from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("这是我的第一个web界面！")
# Create your views here.
#使用django编写web页面时，首先要在views.py中添加各个应用，我理解为行为（action），
#1.先定义一个函数，函数要有参数，函数内部执行我们需要的行为
#2.在将views中的行为函数定义好之后，要在myblog文件夹下的settings.py文件中
#找到INSTALLED_APPS，在其中添加我们刚刚构建的新的action函数
#3.最后在urls.py文件中添加相应的url
#4.在命令行下运行runserver,在浏览器中输入相应的HTTP访问