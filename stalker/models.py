from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=60)
    facebook_id = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.name


