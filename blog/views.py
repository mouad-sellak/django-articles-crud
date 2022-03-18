from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Article, Category
from .forms import ArticleForm
# Create your views here.



def index(request):
    articles=Article.objects.all() #objects containts all methodes get filter all, exclude
   #articles=Article.objects.filter(state=1) #objects containts all methodes get filter all, exclude
    categories=Category.objects.all()
    return render(request,'blog/index.html', {'articles':articles, 'categories' : categories} )

def show(request,slug):
    #return HttpResponse(id)
    # my_articale=None
    # for article in data:
    #     if article['id']==id:
    #         my_article=article
    
    # try:
    #     article=Article.objects.get(slug=slug)
    # except:
    #     raise Http404()
    #articles=Article.objects.filter(slug!=slug)
    articles=Article.objects.exclude(slug=slug)
    article=get_object_or_404(Article,slug=slug)
    return render(request,'blog/show.html', {'article':article, 'articles':articles})

def create(request):
    form = ArticleForm #instantiate
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()                                                                                                                                                                                                                                                                                                                                 
            return redirect('list-of-articles')
    return render(request,'blog/create.html', {"form":form})


def edit(request,id):
    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article) #instantiate
    
    if request.method=='POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()                                                                                                                                                                                                                                                                                                                                 
            return redirect('list-of-articles')
    return render(request,'blog/edit.html', {"form":form})

def delete(request,id):
    article=Article.objects.get(pk=id)
    article.delete()
    return redirect('list-of-articles')


# def delete(request,id):
#     article=Article.objects.get(pk=id)
#     articles=Article.objects.all()
#     if request.method=='POST':
#         #articles=[art for art in articles if art!=article]
#         article.delete()
#         print('-----------------------------------------')
#         print(articles)
#         print('-----------------------------------------')
#     return render(request,'blog/index.html', {'articles':articles})
