from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

class display_list(admin.ModelAdmin):
    list_display = ('title','content','img1','published_date','update_at')

admin.site.register(Post,display_list)