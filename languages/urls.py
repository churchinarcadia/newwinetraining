from django.urls import path

from . import views

app_name = 'languages'
urlpatterns = [
    path('language/index/', views.language_index, name = 'language_index'),
    path('language/add/', views.language_add, name = 'language_add'),
    path('language/edit/', views.language_edit, name = 'language_edit'),
    path('language/delete/', views.language_delete, name = 'language_delete'),
    path('translation/index/', views.translation_index, name = 'translation_index'),
    path('translation/add/', views.translation_add, name = 'translation_add'),
    path('translation/edit/', views.translation_edit, name = 'translation_edit'),
    path('translation/delete/', views.translation_delete, name = 'translation_delete'),
    path('translator/index/', views.translator_index, name = 'translator_index'),
    path('translator/add/', views.translator_add, name = 'translator_add'),
    path('translator/edit/', views.translator_edit, name = 'translator_edit'),
    path('translator/delete/', views.translator_delete, name = 'translator_delete'),
]