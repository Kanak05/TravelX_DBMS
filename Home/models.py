from django.db import models

# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	image = models.CharField(max_length=200)
	def __str__(self):
		return self.title
	
class Fest(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	image = models.CharField(max_length=200)
	def __str__(self):
		return self.title