from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from users.models import *

class ProfilePermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.method == 'POST':
            return True
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','DELETE','POST','PUT']:
                profile=Profile.objects.filter(user__username=request.user.username).count()>0
                if profile:
                    return True
        return False

def ProfileQuerySet(request):
    if (request.user.username == 'admin'):
        return Profile.objects.all()
    profile=Profile.objects.filter(user__username=request.user.username)
    if profile.count()>0:
        return Profile.objects.filter(corp__user__username=request.user.username)
    return Profile.objects.none()


class GroupPermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method == 'POST':
                return True
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','DELETE','PUT']:
                teacher=Group.objects.filter(teacher__user__username=request.user.username).count()>0
                student=Group.objects.filter(student__user__username=request.user.username).count()>0
                if teacher or (student):# and request.method == 'GET'):
                    return True
        return False

def GroupQuerySet(request):
    if (request.user.username == 'admin'):
        return Group.objects.all()
    group=Group.objects.filter(Q(teacher__user__username=request.user.username) | Q(student__user__username=request.user.username))
    if request.method == 'GET':
        return group
    if request.method in ['PUT','DELETE']:
        return group.filter(teacher__user__username=request.user.username)
    return Group.objects.none()