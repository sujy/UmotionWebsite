from django.db import models
from User.models import User
# Create your models here.
class RoadMap(models.Model):
    time = models.DateField(blank=True)
    content = models.TextField(max_length=300)
# branch
class Project(models.Model):
    title = models.TextField(max_length=51200)
    brief = models.TextField(max_length=51200)
    member = models.ManyToManyField(User, related_name='project_member')
    leader = models.ForeignKey(User)
    follower = models.ManyToManyField(User, related_name='project_follower')
    roadmap = models.ForeignKey(RoadMap)
    category = models.CharField(max_length=100)