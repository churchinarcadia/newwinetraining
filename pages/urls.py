from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('/', Index().as_view(), name = 'page_index'),
    path('home/', Index().as_view(), name = 'page_index'),
]