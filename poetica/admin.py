from django.contrib import admin

# Register your models here.

from .models import Poem, Comment, Status

admin.site.register(Poem)
admin.site.register(Comment)
admin.site.register(Status)