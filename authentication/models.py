from django.db import models

# Create your models here.

from datetime import date

class Author(models.Model):
	name = models.CharField(max_length=100, default="unknown")
	date_of_birth = models.DateField(default=date(1900,1,1))

	def __str__(self):
		return self.name


class BooksInfo(models.Model):
	book_title = models.CharField(max_length=100, null=True)
	release_date = models.DateField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE,)
	price = models.IntegerField()
	short_description = models.TextField()
	
	def __str__(self):
		return self.name
