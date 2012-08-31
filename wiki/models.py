#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

from datetime import datetime, timedelta
import pytz

def default_now():
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    # Essa merda de UTC só funciona direito na versão 1.4 :(
    # Era fazer essa gambi ou modificar o código do nonrel
    now = now - timedelta(hours=3)
    
    return now 

class Page(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    
    data = models.TextField()
    
    updated = models.DateTimeField()
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.updated = default_now()
        super(Page, self).save()


class PageAdmin(admin.ModelAdmin):
    exclude = ('updated',)
    
admin.site.register(Page,PageAdmin)    