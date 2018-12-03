# -*- coding:utf-8 -*-
__author__ = 'WhaleFall'
__date__ = '2018-11-28 22:26'

import xadmin
from .models import UserFile
from .models import EmailVerifyRecord
from .models import Banner
class UserFileAdmin(object):
    list_diplay = ['nick_name','birthday','gender','address','mobile','Image']
    list_filter = ['nick_name','birthday','gender','address','mobile','Image']
    search_fields = ['nick_name','birthday','gender','address','mobile','Image']


class EmailVerifyRecordAdmin(object):
    list_diplay = ['code','email','send_type','send_time']
    list_filter = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_diplay = ['title','image','url','index','add_time']
    list_filter = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.unregister(UserFile)
xadmin.site.register(UserFile,UserFileAdmin)
xadmin.site.register(Banner,BannerAdmin)