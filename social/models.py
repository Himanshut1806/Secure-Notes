from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Note(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200, null=True)
    user= models.ForeignKey(User, on_delete = models.CASCADE)  #If user deleted his account permanently then thier data will be deleted automaticlly thats why use on_delete = CASCADE

    def __str__(self):
        return self.title
    