# -*- coding:utf-8 -*-
__author__ = 'WhaleFall'
__date__ = '2018-12-02 16:15'

from captcha.fields import CaptchaField
from django import forms


class userforms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class resgiterforms(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={'invalid':"验证码错误"})