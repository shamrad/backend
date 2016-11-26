from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView , UpdateView

from .models import Member, Writing



def index(request,username):
    current_user =Member.objects.get(username=username)
    exam=current_user.writing_set.all()

    context={
        'user':current_user,
        'exam':exam
    }
    return render(request, 'user_profile/index.html', context)


def writing(request,username,text_id):
    current_writing=Writing.objects.get(pk=text_id)
    return render(request, 'user_profile/writing page.html',{'object':current_writing})


class CreateWriting(CreateView):
    model = Writing
    fields = ['author','title','text']


class CreateStu(CreateView):
    model = Member
    fields = ['name','username','email']


class EditStu(UpdateView):
    model = Member
    fields = ['name','username','email']
