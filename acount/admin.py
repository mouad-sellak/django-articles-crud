from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','username', 'created_at',)
    list_filter=('state',)
    search_fields=('name','username',)
admin.site.register(Profile,ProfileAdmin)