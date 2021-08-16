from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('usertype/index/', views.usertype_index, name = 'usertype_index'),
    path('usertype/view/<int:usertype_id>/', views.usertype_view, name = 'usertype_view'),
    path('usertype/add/', views.usertype_add, name = 'usertype_add'),
    path('usertype/edit/<int:usertype_id>/', views.usertype_edit, name = 'usertype_edit'),
    path('usertype/delete/<int:usertype_id>/', views.usertype_delete, name = 'usertype_delete'),
    path('locality/index/', views.locality_index, name = 'locality_index'),
    path('locality/view/<int:locality_id>/', views.locality_view, name = 'locality_view'),
    path('locality/add/', views.locality_add, name = 'locality_add'),
    path('locality/edit/<int:locality_id>/', views.locality_edit, name = 'locality_edit'),
    path('locality/delete/<int:locality_id>/', views.locality_delete, name = 'locality_delete'),
    path('user/index/', views.user_index, name = 'user_index'),
    path('user/view/<int:user_id>/', views.user_view, name = 'user_view'),
    path('user/add/', views.user_add, name = 'user_add'),
    path('user/edit/<int:user_id>/', views.user_edit, name = 'user_edit'),
    path('user/delete/<int:user_id>/', views.user_delete, name = 'user_delete'),
]