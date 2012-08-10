from django.db import models
from django.contrib import admin

class WishList(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.name
    
admin.site.register(WishList)    