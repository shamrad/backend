from django.core.urlresolvers import reverse
from django.db import models

class Member(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('user_profile:index', kwargs={'username':self.username})

    def __str__(self):
        return self.name


class Writing(models.Model):
    author=models.ForeignKey(Member,null=False)
    text=models.CharField(max_length=50000,null=False)
    score=models.CharField(max_length=20,null=True, default='0')
    title=models.CharField(max_length=30,null=True,default='untitled')

    def get_absolute_url(self):
        return reverse('user_profile:index', kwargs={'username':self.author.username})

    def __str__(self):
        return self.author.name +'-'+self.title


