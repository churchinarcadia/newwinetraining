from django.urls import path

from . import views

app_name = 'languages'
urlpatterns = [
    path('language/index/', views.language_index, name = 'language_index'),
    path('language/view/<int:language_id>/', views.language_view, name = 'language_view'),
    path('language/add/', views.language_add, name = 'language_add'),
    path('language/edit/<int:language_id>/', views.language_edit, name = 'language_edit'),
    path('language/delete/<int:language_id>/', views.language_delete, name = 'language_delete'),
    path('translation/index/', views.translation_index, name = 'translation_index'),
    path('translation/view/<int:translation_id>/', views.translation_view, name = 'translation_view'),
    path('translation/add/', views.translation_add, name = 'translation_add'),
    path('translation/edit/<int:translation_id>/', views.translation_edit, name = 'translation_edit'),
    path('translation/delete/<int:translation_id>/', views.translation_delete, name = 'translation_delete'),
    path('translator/index/', views.translator_index, name = 'translator_index'),
    path('translator/view/<int:translator_id>/', views.translator_view, name = 'translator_view'),
    path('translator/add/', views.translator_add, name = 'translator_add'),
    path('translator/edit/<int:translator_id>/', views.translator_edit, name = 'translator_edit'),
    path('translator/delete/<int:translator_id>/', views.translator_delete, name = 'translator_delete'),
]