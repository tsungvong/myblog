from django.db import models

# Create your models here.
class blogspost(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	timestamp = models.DateTimeField()
