from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from .permissions import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password','email')
        write_only_fields=('password',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields=('id','user','name','image','address','phone')
        read_only_fields=('image',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=str(user_data['username']).lower(),
                            email=str(user_data['email']).lower(),
                            )
        user.set_password(user_data['password'])
        user.save()
        try:
            profile=Profile.objects.create(user=user,
                                name=validated_data.pop('name'),
                                address=validated_data.pop('address'),
                                phone=validated_data.pop('phone'),
                                )
        except:
            User.objects.filter(username=user_data['username']).delete()
        return profile




class GroupRoleSerializerforGroup(serializers.ModelSerializer):
    class Meta:
        model = GroupRole
        fields='__all__'
        read_only_fields=('date_updated','group','profile')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields=('id','name','description','image','date_updated')
        read_only_fields=('date_updated','image')
    
    def create(self, validated_data):
        username=self.context['request'].user.username
        teacher = Profile.objects.get(user__username=username)
        group=Group.objects.create(
                    name=validated_data.pop('name'),
                    description=validated_data.pop('description'),
                    createdBy=teacher
                    )
        return group



class GroupRoleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=None, min_length=None,write_only=True)
    groupid = serializers.CharField(max_length=None, min_length=None,write_only=True)
    group=GroupSerializer(read_only=True)
    profile=ProfileSerializer(read_only=True)
    class Meta:
        model = GroupRole
        fields=('id','username','groupid','group','profile','role','date_updated')
        read_only_fields=('date_updated','group','profile')
    
    def create(self, validated_data):
        username=self.context['request'].user.username
        profile=validated_data.pop('username')
        profile=Profile.objects.filter(user__username=profile)
        group=validated_data.pop('groupid')
        role=validated_data.pop('role')
        if not role.lower() in ['student','teacher']:
            role='student'
        group=Group.objects.filter(id=group , createdBy__user__username=username)
        if group.count()==1 and profile.count()==1:
                exist=GroupRole.objects.filter(group=group[0],profile=profile[0])
                if exist.count()>0:
                    return exist
                grouprole=GroupRole.objects.create(
                        group=group[0],
                        profile=profile[0],
                        role=role
                        )
        try:
            return grouprole
        except:
            return GroupRole.objects.none()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username','')
        password = data.get('password','')

        if username and password:#checking if both are avalable or not
            user = authenticate(username=username,password=password)
            if user:# if user found 
                if user.is_active:# if user is active
                    data['user'] = user #if all correct then we are going to add "user" to given "data" and return 
                else:#if account is not active reise or active the account
                    msg = 'account is not active'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'unable to login with given creds'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Username or Passwords are both required !!!'
            raise exceptions.ValidationError(msg)
        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

