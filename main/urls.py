from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login_, name='login'),
    path('register', views.register_, name='register'),
]
