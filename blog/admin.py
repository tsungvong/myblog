from django.contrib import admin
from blog.models import blogspost

# Register your models here.
class blogpostadmin(admin.ModelAdmin):
	list_display=['title','body','timestamp']

admin.site.register(blogspost,blogpostadmin)