from django.db import models

# Create your models here.

class BooksInfo(models.Model):
	name = models.CharField(max_length=100, null=True)
	release_date = models.DateField()
	author = models.CharField(max_length=100, null=True)
	short_description = models.TextField()
	price = models.IntegerField()
	
	def __str__(self):
		return self.name