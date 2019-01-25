"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
]
#今天学习第二种配置url的方法，这种方法使用include函数，
#1.先导入include包“from django.urls import include,path”
#2.在修改URLpatterens中的path('blog/', include("blog.urls")),第一个参数
#为一级url地址，第二个参数使用include方法，可以引用非根目录下的应用。这样做
#主要是因为：如果将所有的应用都放在根目录myblog目录下，将会导致根目录文件众多
#使用include方法可以在blog目录中新建更多的应用而直接去引用
#3.在blog目录中新建一个python文件，文件名为path的第二个参数
#4.在新建的文件中将根目录中的内容考下来复制进去，在新文件中的path的第一个参数
#是url的二级文件名，第二个参数是调用定义的应用
