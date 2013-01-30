from blog.models import *
from django.contrib import admin

admin.site.register(Category)
admin.site.register(Post, PostAdmin)

admin.site.register(FortuneCookie)
admin.site.register(Links)


