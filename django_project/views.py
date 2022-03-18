from django.http.response import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to learn Django </h1>')

