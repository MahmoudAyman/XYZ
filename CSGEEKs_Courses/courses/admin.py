from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Video)
admin.site.register(Assignment)
admin.site.register(File)