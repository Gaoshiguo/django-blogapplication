from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def book(request):
    return HttpResponse("这是图书首页")


def bookdetail(requets,book_id):
    text = "您请求的book_id为：%s"%book_id
    return HttpResponse(text)


def author_id(request):
    author_id = request.GET.get('id')
    #author_id = request.GET['id']
    text = "您请求的作者id是：%s"%author_id
    return HttpResponse(text)