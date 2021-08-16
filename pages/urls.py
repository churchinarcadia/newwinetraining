from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('/', views.index, name = 'page_index'),
    path('home/', views.index, name = 'page_index'),
]