from django.db import models


# Create your models here.
from user.models import User


class Order(models.Model):
    all_price = models.FloatField('金额')
    state = models.CharField('状态', max_length=10, default='未发货')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'
