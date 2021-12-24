from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
# Create your views here.


def index(request):
    articles=Article.objects.all() #objects containts all methodes get filter all, exclude
   # articles=Article.objects.filter(state=1) #objects containts all methodes get filter all, exclude
    return render(request,'blog/index.html', {'articles':articles} )

def show(request,id):
    #return HttpResponse(id)
    # my_articale=None
    # for article in data:
    #     if article['id']==id:
    #         my_article=article
    article=Article.objects.get(pk=id)
    return render(request,'blog/show.html', {'article':article})

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
