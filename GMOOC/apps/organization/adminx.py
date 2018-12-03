# -*- coding:utf-8 -*-
__author__ = 'WhaleFall'
__date__ = '2018-11-29 21:36'

from .models import CourseOrg,CityDict,Teacher
import xadmin


class CourseOrgAdmin(object):
    list_display = ['name','desc','click','fav_nums','image','address','city','add_time']
    search_fields =['name','desc','click','fav_nums','image','address','city','add_time']
    list_filter = ['name','desc','click','fav_nums','image','address','city','add_time']


class CityDictAdmin(object):
    list_display = ['name','add_time','desc']
    list_filter = ['name','add_time','desc']
    search_fields  = ['name','add_time','desc']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'click', 'add_time',
                    'fav_nums']
    list_filter = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'click', 'add_time',
                   'fav_nums']
    search_fields = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'click', 'add_time',
                     'fav_nums']


xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)

