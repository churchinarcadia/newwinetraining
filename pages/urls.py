from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.page_index, name = 'page_index'),
    path('home/', views.page_index, name = 'page_index'),
]