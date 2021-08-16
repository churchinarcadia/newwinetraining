from django.urls import path

from . import views

app_name = 'languages'
urlpatterns = [
    path('language/index', views.language_index, name = 'language_index'),
    path('language/add', views.language_add, name = 'index'),
    path('language/edit', views.language_edit, name = 'index'),
    path('language/delete', views.language_delete, name = 'index'),
    path('translation/index', views.translation_index, name = 'index'),
    path('translation/add', views.translation_add, name = 'index'),
    path('translation/edit', views.translation_edit, name = 'index'),
    path('translation/delete', views.translation_delete, name = 'index'),
]