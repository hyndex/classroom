from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=True, default = '')
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    verified = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='Profile/',blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.user.username


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Group/',blank=True, null=True)
    students=models.ManyToManyField(Profile,related_name='GroupStudents')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    createdBy = models.ForeignKey(Profile,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name


class GroupRole(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    role = models.TextField(default='Student')
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.name