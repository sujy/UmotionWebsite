from django.db import models

# Create your models here.
#image avator
#project
#post
class User(models.Model):
	username = models.CharField(max_length=100, primary_key=True)
	password = models.CharField(max_length=50)
	email = models.EmailField('e-mail',blank=True)
	phone = models.IntegerField(max_length=12)
	name = models.CharField(max_length=300)
	gender = models.CharField(max_length=10)
	grade = models.IntegerField(max_length=10)
	level = models.IntegerField(max_length=10)
	lastlogin = models.DateField(blank=True, null=True)
	profile = models.TextField(max_length=51200)

	def __unicode__(self):
		return self.name



