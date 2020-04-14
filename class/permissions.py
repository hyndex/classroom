from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *


class NotesPermission(BasePermission):
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
        if request.method in ['DELETE','PUT']:
            if obj.created_by.user.username == request.user.username:
                return True            
        return False

def NotesQuerySet(request):
    if (request.user.username == 'admin'):
        return Notes.objects.all()
    
    membership=GroupRole.objects.filter(profile__user__username=request.user.username,role='student')
    queries = [Q(group__id=member.group.id) for member in membership]
    query = queries.pop()
    for item in queries:
        query |= item


    notes=Notes.objects.filter(Q(created_by__user__username=request.user.username) | query)
    if request.method == 'GET':
        return notes
    if request.method in ['PUT','DELETE']:
        return notes.filter(created_by__user__username=request.user.username)
    return Notes.objects.none()

class AssignmentPermission(BasePermission):
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
        if request.method in ['DELETE','PUT']:
            if obj.created_by.user.username == request.user.username:
                return True            
        return False

def AssignmentQuerySet(request):
    if (request.user.username == 'admin'):
        return Assignment.objects.all()

    membership=GroupRole.objects.filter(profile__user__username=request.user.username,role='student')
    queries = [Q(group__id=member.group.id) for member in membership]
    query = queries.pop()
    for item in queries:
        query |= item

    assignment=Assignment.objects.filter(Q(created_by__user__username=request.user.username) | query)
    if request.method == 'GET':
        return assignment
    if request.method in ['PUT','DELETE']:
        return assignment.filter(created_by__user__username=request.user.username)
    return Assignment.objects.none()


class AssignmentSubmitPermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method == 'POST':
                assignment=Assignment.objects.filter(id=request.data["assignmentid"])
                if not assignment.count()>0:
                    return False
                assignment=assignment[0]
                group=assignment.group.id
                if GroupRole.objects.filter(profile__user__username=request.user.username,group__id=group).count()>0:
                    deadline=int(assignment.deadline)
                    today=dt.date.today()
                    if int(str(today.year)+str(today.month)+str(today.day)) > deadline:
                        return False
                    return True
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','DELETE','PUT']:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE','PUT']:
            if obj.student.user.username == request.user.username:
                deadline=obj.assignment.deadline
                today=dt.date.today()
                if  int(str(today.year)+str(today.month)+str(today.day)) < deadline:
                    return True            
        return False


def AssignmentSubmitQuerySet(request):
    if (request.user.username == 'admin'):
        return AssignmentSubmit.objects.all()
    assignment=AssignmentSubmit.objects.filter(Q(student__user__username=request.user.username) | Q(assignment__created_by__user__username=request.user.username))
    if request.method in ['PUT','DELETE']:
        return assignment.filter(created_by__user__username=request.user.username)
    if request.method == 'GET':
        return assignment
    return AssignmentSubmit.objects.none()