from django.db import models

# Create your models here.
class Publisher(models.Model):
    name =models.CharField(max_length=30,verbose_name='名称')
    address =models.CharField(max_length=50,verbose_name='地址')
    city=models.CharField(max_length=60,verbose_name='城市')
    state_province =models.CharField(max_length=30,verbose_name='省')
    country = models.CharField(max_length=50,verbose_name='国家')
    website =models.URLField(verbose_name='网址')
    class Meta:
        verbose_name = '出版商'
        verbose_name_plural =verbose_name

    def __str__(self): #接收父类方法
        return self.name#替换掉父类名字


class Author(models.Model):
    name=models.CharField(max_length=30)
    class Meta:
        verbose_name = '作者'
        verbose_name_plural =verbose_name

class AuthorDetail(models.Model):
    sex=models.BooleanField(max_length=1,choices=((0,'男'),(1,'女')))
    email = models.EmailField()
    address= models.CharField(max_length=50)
    birthday= models.DateField()
    author= models.OneToOneField(Author)
    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural =verbose_name





class Book(models.Model):
    title =models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0)#5个数字(含小数)，2位小数
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural =verbose_name

    def __str__(self): #接收父类方法
        return self.title#替换掉父类名字
