from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','slug','vote', 'created_at']
    list_filter=('state',)
    filter_horizontal=('tags',) #just for many to many
admin.site.register(Project,ProjectAdmin)
