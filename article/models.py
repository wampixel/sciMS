from django.db import models
import datetime
# Create your models here.
class Categories(models.Model):
    id  = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=50)

class Articles(models.Model):
    id         = models.AutoField(primary_key=True)
    title      = models.CharField(max_length=50)
    author     = models.CharField(max_length=50)
    add_date   = models.DateField('add_date', default=datetime.date.today)
    date_pub   = models.DateField('date published')
    categories = models.ForeignKey('categories', on_delete=models.CASCADE)
    abstract   = models.CharField(max_length=1000)
    keyword    = models.CharField(max_length=1000)
    content    = models.CharField(max_length=100000)
    ref        = models.CharField(max_length=1000)
    writer     = models.IntegerField(default=0)
    summary    = models.CharField(max_length=1000, default="")