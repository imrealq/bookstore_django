from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class BooksInfo(models.Model):
	name = models.CharField(max_length=100, null=True)
	release_date = models.DateField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	short_description = models.TextField()
	price = models.IntegerField()
	
	def __str__(self):
		return self.name
