
#这个工程用于展示使用django来实现搭建一个blog#</br>
*开发工具：pycahrm+mysql*</br>
*开发环境：python3.7+django3.0+mysql18.0[mysql18.0下载链接](https://dev.mysql.com/downloads/mysql/)*</br>
**预备工作：**</br>1.下载django3.0.可以通过`pip install django -3.0`</br>2.下载MySQL </br>需要注意的是：django3.0与mysql8.0不兼容，解决方法见[链接](https://www.cnblogs.com/gaoshiguo/p/12272980.html)</br>
#第一节：django热身#</br>
首先，打开pycharm,新建一个django工程</br>
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/1.png)</br>
创建后的项目目录如下图所示：
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/3.png)</br>
**初探django：**
然后我们运行这个项目，在pycharm中点击run
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/4.png)</br>
然后在浏览器中输入`127.o.o.1:8000`，就可以看到如下页面：
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/5.png)</br>
**配置django的MySQL数据库：**
首先创建一个数据库，然后配置`setings.py`文件中的数据库
我们只需要更改`setings.py`文件中的`datebase`部分，
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#这里将django.db.backends.sqlite该为MySQL
        'NAME': 'myblog',#这里填创建的数据库名称
        'USER':'root',#这里填MySQL数据库的user
        'PASSWORD':'123456',#这里填MySQL数据库的密码
        'HOST':'127.0.0.1',#这里填本机地址
        'PORT':'3306',#这里填数据库的端口号
    }
 ```
**小试牛刀**</br>
首先开始写一个user模块，该模块的主要功能是实现用户的登录和注册，上一节已经介绍了如何配置数据库。</br>
开始用户模块之前，我们需要创建一个app,并且需要在`setings.py`文件的
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
部分添加这个新建的app，</br>在django中创建app的方式由两种：1，通过cmd终端创建2.通过pycharm创建</br>
1.通过cmd终端创建app
首先cmd 进入项目所在目录，然后运行命令：`python manage.py startapp user`
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/7.png)</br>
运行完这个命令后就可以看到自动的生成了一个文件夹user
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/8.png)</br>


