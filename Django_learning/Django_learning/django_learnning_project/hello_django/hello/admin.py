from django.contrib import admin
from .models import *#引入同文件下的模块打.


# Register your models here.
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publisher)
admin.site.register(Book)


