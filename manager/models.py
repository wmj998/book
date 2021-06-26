from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField('书名', max_length=50, unique=True)
    book_price = models.FloatField('价格')
    book_author = models.CharField('作者', max_length=20)
    book_sales = models.IntegerField('销量')
    book_stock = models.IntegerField('库存')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'book'
