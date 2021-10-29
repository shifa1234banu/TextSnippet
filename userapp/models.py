from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.CharField(max_length=100)        

    def __str__(self):
        return self.title


class Textsnippet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.title


