from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Log(models.Model):
    time = models.DateTimeField()
    clinetip = models.GenericIPAddressField(default=None)
    retserver = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        if self.time:
            t = self.time.strftime('%m-%d-%y %H:%M:%S')
        else:
            t = 'None'
        return t
