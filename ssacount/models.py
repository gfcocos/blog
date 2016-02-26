from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    #python2 use __unicode__, python3 use __str__
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class SSAcount(models.Model):
    server = models.CharField(max_length=50)
    server_port = models.CharField(max_length=50)
    server_aes = models.CharField(max_length=50,default='',blank=True)
    method = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    ping = models.IntegerField()
    url = models.CharField(max_length=100,default='',blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.server
