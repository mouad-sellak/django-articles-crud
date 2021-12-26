from django.contrib import admin
from .models import Article,Author
from .models import Category
from .models import Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','slug','category', 'created']
    list_filter=['category']
    
admin.site.register(Article, ArticleAdmin) 


#admin.site.register(Article) tjwj :))
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
