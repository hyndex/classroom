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


class AssignmentSubmitUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated:
            if request.method in ['POST','PUT']:
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