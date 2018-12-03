from django.db import models
from datetime import  datetime
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'课程名')
    desc = models.CharField(max_length=50,verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')),max_length= 2,verbose_name=u'难度')
    learn_time = models.IntegerField(default=0,verbose_name=u'学习时长')
    students = models.IntegerField(verbose_name=u'学习人数',default=0)
    fav_num = models.IntegerField(verbose_name=u'收藏人数',default=0)
    image = models.ImageField(upload_to='courses%Y/%m',verbose_name=u'封面图',max_length=1)
    click_number = models.IntegerField(default=0,verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')


    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=100,verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频信息'
        verbose_name_plural = verbose_name

class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'课程')
    name = models.CharField(max_length=100,verbose_name=u'视频名')
    download = models.FileField(max_length= 100 ,upload_to=  'course/resource/%Y/%m',verbose_name=u'上传地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name