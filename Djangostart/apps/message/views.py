from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    if request.method == 'POST':
        usermessage = UserMessage()
        usermessage.email = request.POST.get('email',' ')
        usermessage.name = request.POST.get('name',' ')
        usermessage.adress = request.POST.get('address',' ')
        usermessage.message = request.POST.get('message',' ')
        usermessage.save()
    return render(request,'get_format.html')