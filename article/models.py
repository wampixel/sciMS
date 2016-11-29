from django.db import models

# Create your models here.
class categories(models.Model):
    id  = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=50)

class article(models.Model):
    title      = models.CharField(max_length=50)
    author     = models.CharField(max_length=50)
    date_pub   = models.DateField('date published')
    categories = models.ForeignKey('categories', on_delete=models.CASCADE)
    abstract   = models.CharField(max_length=1000)
    keyword    = models.CharField(max_length=1000)
    content    = models.CharField(max_length=100)
    ref        = models.CharField(max_length=1000)