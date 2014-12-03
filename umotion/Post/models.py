from django.db import models
from User.models import User
from Project.models import Project,RoadMap

# Create your models here.
class Post(models.Model):
    topic=models.CharField(max_length=300)
    leader=models.ForeignKey(User)
    category=models.CharField(max_length=300)
    content=models.TextField(max_length=51200)
    time=models.DateField()
    project=models.ForeignKey(Project)

class Comment(models.Model):
    user=models.ForeignKey(User)
    content=models.TextField(max_length=51200)
