
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
2.通过pycharm创建，在pycahrm 的tool工具栏里有一个`Run manage.py Task`与1是同样的功效
创建完user app 后需要在需要在`setings.py`文件安装这个app，也就是在
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user'#加上刚刚创建的userapp
]
```
准备工作做好之后，我们来通过ORM创建一张数据库用户表，django已经自动的为我们创建了models.py文件
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/9.png)</br>
我们在`models.py`文件中创建数据库表：</br>
```python
# Create your models here.
class user(models.Model):#创建user数据表，表中三个字段：id,username,password
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,null=False)
    password=models.IntegerField(null=False)
    class Meta:
        db_table = 'user'#设置数据表的表名
 ```
 创建好用户表之后，需要我们进行数据迁移(migrate)，将创建后的user表映射到我们的mysql数据库之中，具体步骤是：cd 进入项目工程所在文件夹下的manage.py
 然后执行：`python manage.py makemigrations user` 和`python manage.py migrate`
 ![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/10.png)</br>
 ![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/11.png)</br>
 执行迁移脚本文件后会发现我们创建的数据库中会多出来一张表：</br>
![](https://github.com/Gaoshiguo/django-blogapplication/blob/master/%E6%88%AA%E5%9B%BE/12.png)</br> 
**搭建前台页面**</br>
我们在myblog目录下的templates文件夹中创建我们的前端html页面。需要注意的是，在django中前端页面的HTML是一个DTL模板，模板之间是可以实现继承。
因此我们使用bootstrap来进行样式的设计，当然这不是重点。</br>
我们先写一个父模板，这样子模板可以通过继承来实现与父模板相同的内容，大大减少了代码量：
父模板文件见链接：

