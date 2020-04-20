from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser, FileUploadParser
from rest_framework.decorators import action
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import datetime as dt


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    search_fields = ['title','description','group__id','group__name']
    filterset_fields = ['group__id','group__name']
    ordering_fields = ['title','created_by','date_updated']
    # ordering=('-date_updated',)
    # filter_fields = ['name','category','instructor','institute']
    serializer_class = NotesSerializer
    permission_classes = [NotesPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return NotesQuerySet(self.request)

class NotesUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                instance=Notes.objects.get(id=pk)
                up_file  = request.FILES['file']
                up_file.name=str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                instance.file=up_file
                instance.save()
                return Response({"success"},status=204)
            if request.method in ['PUT','DELETE']:
                teacher=Notes.objects.filter(created_by__user__username=request.user.username,id=pk)
                if teacher.count()>0 :
                    instance=Notes.objects.get(id=pk)
                    up_file  = request.FILES['file']
                    up_file.name=str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                    instance.file=up_file
                    instance.save()
                    return Response({"success"},status=204)
                else:
                    return Response({"not found"},status=404)




class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    search_fields = ['title','description','group__id','group__name','deadline','created_by__user__username']
    ordering_fields = ['title','created_by','group__id','group__name','date_updated','deadline']
    filterset_fields = ['title','created_by__user__username','group__id','group__name','date_updated','deadline']
    # filterset_fields  = ['group__id',]
    # ordering=('-date_updated',)
    # filter_fields = ['name','category','instructor','institute']
    serializer_class = AssignmentSerializer
    permission_classes = [AssignmentPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return AssignmentQuerySet(self.request)

class AssignmentUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                instance=Assignment.objects.get(id=pk)
                up_file  = request.FILES['file']
                up_file.name=str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                instance.file='process'+str(dt.datetime.now())
                instance.file=up_file
                instance.save()
                return Response({"success"},status=204)
            if request.method in ['PUT','DELETE']:
                assignment=Assignment.objects.filter(created_by__user__username=request.user.username,id=pk)
                if assignment.count()>0 :
                    if request.metod=='PUT':
                        instance=assignment[0]
                        up_file  = request.FILES['file']
                        up_file.name=str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                        instance.file='process'+str(dt.datetime.now())
                        instance.file=up_file
                        instance.save()
                        return Response({"success"},status=204)
                    elif request.method=='DELETE':
                        instance=assignment[0]
                        instance.file=None
                        instance.save()
                        return Response({"success"},status=204)
                else:
                    return Response({"not found"},status=404)





class AssignmentSubmitViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmit.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    search_fields = ['title','description','assignment__id','assignment__group__name','assignment__deadline','assignment__created_by__user__username','student__user__username','student__user__name','student__phone']
    ordering_fields = ['assignment__id','assignment__group__name','assignment__deadline','assignment__created_by__user__username','date_updated']
    # ordering=('-date_updated',)
    # filter_fields = ['name','category','instructor','institute']
    serializer_class = AssignmentSubmitSerializer
    permission_classes = [AssignmentSubmitPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return AssignmentSubmitQuerySet(self.request)


class AssignmentSubmitUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            if (request.user.username == 'admin'):
                instance=AssignmentSubmit.objects.get(id=pk)
                up_file  = request.FILES['file']
                up_file.name=str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                instance.file='process'+str(dt.datetime.now())
                instance.file=up_file
                instance.save()
                return Response({"success"},status=204)
            if request.method in ['PUT','DELETE']:
                assignment=AssignmentSubmit.objects.filter(assignment__group__students__user__username=request.user.username,id=pk)
                if assignment.count()>0 :
                    instance=assignment[0]
                    up_file  = request.FILES['file']
                    up_file.name=str(instance.id)+'.'+str(up_file.name).split(".")[-1]
                    instance.media='process'+str(dt.datetime.now())
                    instance.file=up_file
                    instance.save()
                    return Response({"success"},status=204)
                else:
                    return Response({"not found"},status=404)


