from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt


class Photos(models.Model):
    image = models.ImageField(upload_to='Profile/',blank=True, null=True)
    student= models.ForeignKey(User, on_delete=models.CASCADE)
    datetime=models.DateTimeField(dt.datetime.now())
    status=models.CharField(max_length=10)
