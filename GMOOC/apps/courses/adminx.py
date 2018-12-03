# -*- coding:utf-8 -*-
__author__ = 'WhaleFall'
__date__ = '2018-11-29 22:06'


import xadmin
from .models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    list_fields = ['name','desc','detail','degree','learn_time','students','fav_num','image','click_number','add_time']
    list_display = ['name','desc','detail','degree','learn_time','students','fav_num','image','click_number','add_time']
    search_filter = ['name','desc','detail','degree','learn_time','students','fav_num','image','click_number','add_time']


class LessonAdmin(object):
    list_fields = ['course','name','add_time']
    list_display = ['course','name','add_time']
    search_filter = ['course','name','add_time']


class VideoAdmin(object):
    list_fields = ['lesson', 'name', 'add_time']
    list_display = ['lesson', 'name', 'add_time']
    search_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_fields = ['course', 'name', 'download','add_time']
    list_display = ['course', 'name', 'download','add_time']
    search_filter = ['course', 'name', 'download','add_time']


xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Video,VideoAdmin)