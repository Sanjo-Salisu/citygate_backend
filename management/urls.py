from django.urls import path
from . import views



urlpatterns = [
     path('add_user/', views.add_user, name='add_user'),
     path('gallery_crud/', views.gallery_crud, name='gallery_crud'),
     path('user_list/', views.user_list, name='user_list'),
     path('delete/<int:pk>/', views.delete_image, name='delete_image'),
     path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
     path('add_profile/', views.add_profile, name='add_profile'),
     path('add_management_update/', views.add_management_update, name='add_management_update'),
     path('management_updates/', views.management_updates_list, name='management_updates_list'),
     path('delete_management_update/<int:pk>/', views.delete_management_update, name='delete_management_update'),
     path('gallery_list/', views.gallery_list, name='gallery_list'),
     path('gallery/delete/<int:pk>/', views.delete_image, name='delete_image'),
     path("add_career/", views.add_career, name="add_career"),
     path("career_list/", views.career_list, name="career_list"),
     path("delete_career/<int:pk>/", views.delete_career, name="delete_career"),


   ]
