from django.db import models


# Create your models here.
from user.models import User


class Cart(models.Model):
    book_name = models.CharField('书名', max_length=50)
    number = models.IntegerField('数量')
    one_price = models.FloatField('单价')
    all_price = models.FloatField('总价')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'
