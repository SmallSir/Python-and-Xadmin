from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.
from .models import UserFile
from .forms import userforms,resgiterforms
from django.contrib.auth.hashers import make_password


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserFile.objects.get(Q(username = username)|Q(email = username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class RegisterView(View):
    def get(self,request):
        resgiter_form = resgiterforms()
        return render(request,'register.html',{'register_form':resgiter_form})

    def post(self,request):
        resgiter_form = resgiterforms(request.POST)
        if resgiter_form.is_valid():
            user_name = request.POST.get('username', '')
            user_password = request.POST.get('password', '')
            user_email = request.POST.get('email','')
            user_file = UserFile()
            user_file.username = user_name
            user_file.email = user_email
            user_file.password = make_password(user_password)
            user_file.save()
        else:
            pass

class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form = userforms(request.POST)
        if login_form.is_valid(): #判断是否输入的账号密码存在空值或者少于或者长于某个字段
            user_name = request.POST.get('username', '')
            user_password = request.POST.get('password', '')
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'msg':"账号或者密码错误"})
        else:
            return render(request, 'login.html', {'login_form': login_form, 'msg': "账号或者密码错误"})

