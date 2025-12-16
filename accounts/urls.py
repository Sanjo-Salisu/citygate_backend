from django.urls import path
from . import views


app_name = 'management'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]
