from django.core.urlresolvers import reverse_lazy
from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView , UpdateView, DeleteView

from .models import Member, Writing



def index(request,username):
    current_user =Member.objects.get(username=username)
    exam=current_user.writing_set.all()

    context={
        'user':current_user,
        'exam':exam
    }
    return render(request, 'user_profile/index.html', context)


def writing(request,username,pk):
    current_writing=Writing.objects.get(pk=pk)
    return render(request, 'user_profile/writing page.html',{'object':current_writing})


class CreateWriting(CreateView):
    model = Writing

    def form_valid(self, form):
        auth = Member.objects.get(id=self.kwargs['username'])
        writing.author = auth
        return super(CreateWriting, self).form_valid(form)
    fields = ['title','text']


class CreateStu(CreateView):
    model = Member
    fields = ['name','username','email']


class EditStu(UpdateView):
    model = Member
    fields = ['name','username','email']

class WritingDelete(DeleteView):
    model = Writing
    success_url = reverse_lazy('user_profile:index')