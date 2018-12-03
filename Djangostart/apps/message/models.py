# _*_
from django.db import models

# Create your models here.


class UserMessage(models.Model):
    id_message = models.AutoField(primary_key=True,verbose_name=u'主键')
    name = models.CharField(max_length=20,verbose_name=u'姓名')
    email = models.EmailField(verbose_name=u'邮箱')
    adress = models.CharField(max_length=20,verbose_name=u'联系地址')
    message = models.CharField(max_length=500,verbose_name=u'留言信息')

    class Meta:
        verbose_name = u'留言箱'