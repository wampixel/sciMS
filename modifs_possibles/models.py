from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	categorie = models.CharField(max_length=50)
	abstract = models.CharField(max_length=1000)
	key_word = models.CharField(max_length=100)
	content = models.CharField(max_length=5000)
	ref = models.CharField(max_length=1000)
