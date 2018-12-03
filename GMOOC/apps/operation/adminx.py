# -*- coding:utf-8 -*-
__author__ = 'WhaleFall'
__date__ = '2018-11-29 21:49'



import xadmin
from .models import UserAsk,CourseComments,UserMessage,UserFavorite,UserCourse


class UserAskAdmin(object):
    list_filter = ['name','mobile','add_time','course_name']
    list_display = ['name','mobile','add_time','course_name']
    search_fields = ['name','mobile','add_time','course_name']


class CourseCommentsAdmin(object):
    list_filter = ['user','course','comments','add_time']
    list_display = ['user','course','comments','add_time']
    search_fields = ['user','course','comments','add_time']


class UserFavoriteAdmin(object):
    list_filter = ['user', 'fav_id','fav_type','add_time']
    list_display = ['user', 'fav_id','fav_type','add_time']
    search_fields = ['user', 'fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    list_filter = ['user', 'add_time','message','has_read']
    list_display = ['user', 'add_time','message','has_read']
    search_fields = ['user', 'add_time','message','has_read']


class UserCourseAdmin(object):
    list_filter = ['user','course','add_time']
    list_display = ['user','course','add_time']
    search_fields = ['user','course','add_time']


xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)












