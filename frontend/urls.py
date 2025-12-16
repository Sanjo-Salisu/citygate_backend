from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('loan/', views.loan, name='loan'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('branch/', views.branch, name='branch'),
    path('terms/', views.terms, name='terms'),
    path('gallery/', views.gallery_frontend, name='gallery_frontend'),
    path("send_message/", views.send_message, name="send_message"),
]

