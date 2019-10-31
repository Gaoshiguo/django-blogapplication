from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def movie(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("这是电影首页")
    else:
        return redirect('/book/')


def moviedetail(requets,movie_id):
    text = "您请求的movie_id为：%s"%movie_id
    return HttpResponse(text)


def author_id(request):
    author_id = request.GET.get('id')
    #author_id = request.GET['id']
    text = "您请求的作者id是：%s"%author_id
    return HttpResponse(text)