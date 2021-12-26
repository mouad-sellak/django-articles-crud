from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='list-of-articles'),
    path('<slug:slug>', views.show, name='show-article'), # slug  str
    path('create', views.create, name='create-article'), # slug  str
    path('edit<int:id>', views.edit, name='edit-article'), # slug  str
    path('delete<int:id>', views.delete, name='delete-article') # slug  str
]
