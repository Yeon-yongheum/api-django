from django.contrib import admin

from .models import Music, Artist, Review
# Register your models here.

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Review)
