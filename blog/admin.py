from django.contrib import admin
from .models import Article,Author
from .models import Category
from .models import Tag
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','slug','category', 'created']
    list_filter=['category']
    list_per_page=2
    
admin.site.register(Article, ArticleAdmin) 


#admin.site.register(Article) tjwj :))
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
