from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from .permissions import *

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields=('group','title','description','file')
        read_only_fields=('date_updated','created_by','file')
        
    def create(self, validated_data):
        username = self.context['request'].user.username
        group = validated_data.pop('group')
        date_updated=str(dt.datetime.now())
        profile=Profile.objects.get(user__username=username)
        group=Group.objects.get(id=group)
        assignment = AssignmentSubmit.objects.create(created_by=profile,group=group,date_updated=date_updated,**validated_data)
        return assignment

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.date_updated=str(dt.datetime.now())
        instance.save()
        return instance

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields=('group','title','description','deadline','file','created_by','date_updated')
        read_only_fields=('date_updated','created_by','file')

    def create(self, validated_data):
        username = self.context['request'].user.username
        group = validated_data.pop('group')
        date_updated=str(dt.datetime.now())
        profile=Profile.objects.get(user__username=username)
        group=Group.objects.get(id=group)
        assignment = AssignmentSubmit.objects.create(created_by=profile,date_updated=date_updated,group=group,**validated_data)
        return assignment

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.date_updated=str(dt.datetime.now())
        instance.save()
        return instance

class AssignmentSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmit
        fields=('assignment','title','description','file','student','date_updated')
        read_only_fields=('date_updated','student','file')
    
    def create(self, validated_data):
        username = self.context['request'].user.username
        assignment = validated_data.pop('assignment')
        profile=Profile.objects.get(user__username=username)
        assignment=Assignment.objects.get(id=assignment)
        date_updated=str(dt.datetime.now())
        ass_submit = AssignmentSubmit.objects.create(date_updated=date_updated,student=profile,assignment=assignment,**validated_data)
        return ass_submit

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.date_updated=str(dt.datetime.now())
        instance.save()
        return instance


