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
                teacher=Notes.objects.filter(group__teacher__user__username=request.user.username).count()>0
                student=Notes.objects.filter(group__students__user__username=request.user.username).count()>0
                if teacher or (student):# and request.method == 'GET'):
                    return True
        return False

def NotesQuerySet(request):
    if (request.user.username == 'admin'):
        return Notes.objects.all()
    notes=Notes.objects.filter(Q(created_by__user__username=request.user.username) | Q(group__teacher__user__username=request.user.username) | Q(group__students__user__username=request.user.username))
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
                teacher=Assignment.objects.filter(group__teacher__user__username=request.user.username).count()>0
                student=Assignment.objects.filter(group__students__user__username=request.user.username).count()>0
                if teacher or (student):# and request.method == 'GET'):
                    return True
        return False

def AssignmentQuerySet(request):
    if (request.user.username == 'admin'):
        return Assignment.objects.all()
    assignment=Assignment.objects.filter(Q(created_by__user__username=request.user.username) | Q(group__teacher__user__username=request.user.username) | Q(group__students__user__username=request.user.username))
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
                return True
            if (request.user.username == 'admin'):
                return True
            if request.method in ['GET','DELETE','PUT']:
                teacher=AssignmentSubmit.objects.filter(assignment__group__teacher__user__username=request.user.username).count()>0
                student=AssignmentSubmit.objects.filter(assignment__group__students__user__username=request.user.username).count()>0
                if teacher or (student):# and request.method == 'GET'):
                    return True
        return False

def AssignmentSubmitQuerySet(request):
    if (request.user.username == 'admin'):
        return AssignmentSubmit.objects.all()
    assignment=AssignmentSubmit.objects.filter(Q(student__user__username=request.user.username) | Q(assignment__group__teacher__user__username=request.user.username))
    if request.method in ['PUT','DELETE']:
        return assignment.filter(created_by__user__username=request.user.username)
    if request.method == 'GET':
        return assignment
    return AssignmentSubmit.objects.none()