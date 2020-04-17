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
            if request.method=='POST':
                return False
            if request.method in ['GET','DELETE','PUT']:
                profile=Profile.objects.filter(user__username=request.user.username).count()>0
                if profile:
                    return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.username=='admin':
            return True
        if request.method in ['PUT','DELETE','GET']:
            if obj.user.username == request.user.username:
                return True            
        return False

def ProfileQuerySet(request):
    if (request.user.username == 'admin'):
        return Profile.objects.all()
    profile=Profile.objects.filter(user__username=request.user.username)
    if profile.count()>0:
        return profile
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
                return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.user.username=='admin':
            return True
        if request.method in ['DELETE','GET','PUT']:
            if obj.createdBy.user.username == request.user.username:
                return True            
        return False

def GroupQuerySet(request):
    # return Group.objects.all()
    if (request.user.username == 'admin'):
        return Group.objects.all()
    
    grouprole=GroupRole.objects.filter(profile__user__username=request.user.username)
    if grouprole.count()>0:
        queries = [Q(id=member.group.id) for member in grouprole]
        query = queries.pop()
        for item in queries:
            query |= item
        group=Group.objects.filter(Q(createdBy__user__username=request.user.username) | query)
    else:
        group=Group.objects.filter(Q(createdBy__user__username=request.user.username))

    if request.method == 'GET':
        return group
    if request.method in ['PUT','DELETE']:
        return group.filter(createdBy__user__username=request.user.username)
    return Group.objects.none()



class GroupRolePermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                return True

            if request.method in ['POST','GET','DELETE']:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.username=='admin':
            return True
        if request.method in ['DELETE','GET']:
            if obj.group.createdBy.user.username == request.user.username:
                return True            
        return False

def GroupRoleQuerySet(request):
    if (request.user.username == 'admin'):
        return GroupRole.objects.all()

    # member=GroupRole.objects.filter(profile__user__username=request.user.username)
    # if member.count()>0:
    #     queries = [Q(group__id=value.id) for value in member]
    #     query = queries.pop()
    #     for item in queries:
    #         query |= item
    #     group=GroupRole.objects.filter(Q(group__createdBy__user__username=request.user.username) | query)
    # else:
    #     group=GroupRole.objects.filter(Q(group__createdBy__user__username=request.user.username))

    if request.method in ['GET','DELETE']:
        group=GroupRole.objects.filter(group__createdBy__user__username=request.user.username)
        return group#.filter(group__createdBy__user__username=request.user.username)
    # elif request.method == 'GET':
    #     return group
    return GroupRole.objects.none()